"""Views"""
from django.conf import settings as st
from django.core.validators import RegexValidator, MaxLengthValidator
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, reverse
from django.views.defaults import page_not_found
import markdown

from .models import Queue
from .forms import QueueCreationForm


def home(request):
    context = dict()
    return render(request, template_name="home.html", context=context)


def queue(request, queue_name):
    # validate queue name
    try:
        _ = Queue.validate_name(queue_name)
    except ValidationError as e:
        return page_not_found(request, message=e.message)

    # find queue
    queue = Queue.objects.filter(name=queue_name.lower())
    if not queue:
        return page_not_found(request, message="There is no queue name 'queue'")

    context = dict(
        queue=queue,
    )
    return render(request, template_name="show_queue.html", context=context)


def create_queue(request):
    context = dict(description=markdown.markdown(description))

    return render(request, template_name="create_queue.html", context=context)
