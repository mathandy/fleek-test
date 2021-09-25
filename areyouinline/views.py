"""Views"""
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.views.defaults import page_not_found

from .models import Queue
from .forms import QueueCreationForm, QueueMemberForm


def home(request):
    context = dict()
    return render(request, template_name="home.html", context=context)


def queue(request, queue_name):
    # validate queue name
    try:
        _ = Queue.validate_name(queue_name)
    except ValidationError as e:
        return page_not_found(request=request, exception=e.message)

    # find queue
    queue = Queue.objects.filter(name=queue_name.lower())
    if not queue:
        return page_not_found(
            request=request, exception=f"There is no queue named '{queue_name}'.")

    if request.method == "POST":
        form = QueueMemberForm(data=request.POST)
        if form.is_valid():
            queue.members += f',{form.member_name}'
        return redirect(queue.get_url())

    # render queue page
    context = dict(
        queue=queue,
        form=QueueMemberForm(),
    )
    return render(request, template_name="show_queue.html", context=context)


def create_queue(request):
    context = dict(
        form=QueueCreationForm(),
        existing_queue_names=[q.name for q in Queue.objects.all()]
    )
    return render(request, template_name="create_queue.html", context=context)
