from django import forms

from .models import Queue


class QueueCreationForm(forms.Form):
    name = forms.CharField(label="Queue Name",
                           validators=Queue.validate_name,
                           strip=True,
                           help_text="Enter a name for your new queue.")
    description = forms.CharField(widget=forms.Textarea,
                                  max_length=Queue.DESCRIPTION_MAX_LENGTH,
                                  label="Post Content",
                                  strip=False)
    max_members = forms.IntegerField(label="Post Content",
                                     strip=False)

class QueueMemberForm(forms.Form):
    member_name = forms.CharField(label="Queue Name", validators=Queue.validate_name,
                                  help_text="Enter a name for your new queue.")