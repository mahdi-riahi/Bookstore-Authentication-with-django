from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(
        blank=False,
        null=False,
        unique=True,
        verbose_name='Email Address',
        error_messages={'unique': 'This email address has been registered. You need your email for restore your account'}
    )
    nat_id = models.CharField(
        max_length=10,
        blank=False,
        null=False,
        unique=True,
        verbose_name='National ID',
        validators=[
            RegexValidator(
                regex='^[0-9]{10}$',
                message='National ID has to be 10 digits exactly',
                code='invalid_national_code'
            ),
        ],
        error_messages={
            'unique': 'This ID has been signup before'
        }
    )
