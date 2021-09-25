from django.db import models
from django.contrib import admin

from martor.widgets import AdminMartorWidget

from .models import Queue, QueueMember


@admin.register(Queue)
class QueueAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


@admin.register(QueueMember)
class QueueMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'queue', 'join_datetime',)
