"""Views"""
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.views.defaults import page_not_found

from .models import Queue, QueueMember
from .forms import QueueCreationForm, QueueMemberForm


def home(request):
    context = dict()
    return render(request, template_name="home.html", context=context)


def show_queue(request, queue_name):
    # validate queue name
    try:
        _ = Queue.validate_name(queue_name)
    except ValidationError as e:
        return page_not_found(request=request, exception=e.message)

    # find queue
    queue = Queue.objects.filter(name=queue_name.lower()).first()
    if not queue:
        return page_not_found(
            request=request, exception=f"There is no queue named '{queue_name}'.")

    if request.method == "POST":
        form = QueueMemberForm(data=request.POST)
        if form.is_valid():
            QueueMember(name=form.cleaned_data.get('member_name'), queue=queue).save()
        return redirect(queue.url)

    # render queue page
    context = dict(
        queue=queue,
        form=QueueMemberForm(),
        members=list(QueueMember.objects.filter(queue=queue)),
    )
    return render(request, template_name="show_queue.html", context=context)


def create_queue(request):
    initial = dict(max_members=100)
    form = QueueCreationForm(data=request.GET, initial=initial)
    if request.method == "POST":
        form = QueueCreationForm(data=request.POST)
        from IPython import embed; embed()  ### DEBUG
        if form.is_valid():
            queue = Queue(
                name=form.cleaned_data.get('name').lower(),
                description=form.cleaned_data.get('description'),
                max_members=form.cleaned_data.get('max_members'),
            )
            queue.save()
            return redirect(queue.url)
    context = dict(
        form=form,
        existing_queue_names=[q.name for q in QueueMember.objects.all()]
    )
    return render(request, template_name="create_queue.html", context=context)


def about(request):
    return render(request, template_name="about.html")
