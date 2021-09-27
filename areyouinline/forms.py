from django import forms

from .models import Queue
from martor.fields import MartorFormField


class QueueCreationForm(forms.Form):
    name = forms.CharField(
        label="Name for queue",
        help_text="Enter a name for your new queue.",
        validators=[Queue._allowed_chars_validator],
        strip=True,
        max_length=Queue.NAME_MAX_LENGTH,
    )
    description = MartorFormField(
        label="Description of queue",
        help_text="Explain what this queue is for.",
        max_length=Queue.DESCRIPTION_MAX_LENGTH,
    )
    max_members = forms.IntegerField(
        label="Max Members allowed in queue",
        help_text="Enter the maximum number of members to allow in queue.",
        min_value=1,
    )


class QueueMemberForm(forms.Form):
    member_name = forms.CharField(
        label="Add a name to the queue:",
        help_text="Enter a name for your new queue.",
        validators=[Queue._allowed_chars_validator],
        max_length=Queue.MEMBER_NAME_MAX_LENGTH,
    )
