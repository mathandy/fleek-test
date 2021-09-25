from django.db import models
from django.contrib import admin

from martor.widgets import AdminMartorWidget

from .models import Queue


class QueueAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


admin.site.register(Queue, QueueAdmin)
