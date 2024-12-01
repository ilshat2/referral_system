import random
import string
from django.db import models


class User(models.Model):
    phone = models.CharField(
        max_length=15,
        unique=True
    )
    invite_code = models.CharField(
        max_length=6,
        unique=True,
        blank=True
    )
    activated_invite_code = models.CharField(
        max_length=6,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.invite_code:
            self.invite_code = ''.join(
                random.choices(string.ascii_letters + string.digits, k=6)
            )
        super().save(*args, **kwargs)


class Referral(models.Model):
    inviter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='invited_users'
    )
    invited = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='referral_by'
    )
