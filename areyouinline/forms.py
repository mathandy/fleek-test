from django import forms

from .models import Queue
from martor.fields import MartorFormField


class QueueCreationForm(forms.Form):
    name = forms.CharField(
        label="Queue Name",
        help_text="Enter a name for your new queue.",
        validators=[Queue._allowed_chars_validator],
        strip=True,
        max_length=Queue.NAME_MAX_LENGTH,
    )
    description = MartorFormField(
        label="Queue Description",
        help_text="(Optionally) explain what this queue is for.",
        max_length=Queue.DESCRIPTION_MAX_LENGTH,
    )
    max_members = forms.IntegerField(
        label="Max Members", 
        help_text="The maximum number of members to allow in queue.",
        min_value=1,
    )


class QueueMemberForm(forms.Form):
    member_name = forms.CharField(
        label="Queue Name",
        help_text="Enter a name for your new queue.",
        validators=[Queue._allowed_chars_validator],
        max_length=Queue.MEMBER_NAME_MAX_LENGTH,
    )
