from django.db import models
from django.core.validators import RegexValidator, MaxLengthValidator


class Queue(models.Model):
    objects = models.Manager()

    NAME_MAX_LENGTH = 100
    DESCRIPTION_MAX_LENGTH = 10_000
    MEMBERS_MAX_NUMBER = 25
    MEMBER_NAME_MAX_LENGTH = 32

    _allowed_chars_validator = RegexValidator(
            regex=r"^[a-zA-Z0-9_]*$",
            message="Queue names can only contain letters, numbers, and underscores.",
            code=None,
            inverse_match=None,
            flags=0
        )

    _max_length_validator = MaxLengthValidator(
            limit_value=NAME_MAX_LENGTH,
            message=f"Queue names can be at most {NAME_MAX_LENGTH} characters."
        )

    # fields
    name = models.CharField(null=False, unique=True, max_length=NAME_MAX_LENGTH)
    description = models.CharField(null=True, max_length=DESCRIPTION_MAX_LENGTH)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    max_members = models.PositiveIntegerField(null=False, default=25)
    members = models.CharField(null=False, default='', max_length=MEMBER_NAME_MAX_LENGTH*1000)

    @classmethod
    def validate_name(cls, name):
        _ = cls._max_length_validator(name)
        _ = cls._allowed_chars_validator(name)

    @classmethod
    def validate_member_name(cls, name):
        _ = cls._max_length_validator(name)
        _ = cls._allowed_chars_validator(name)
