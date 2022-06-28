from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class User(AbstractUser):
    pass


class Referral(MPTTModel):
    parent = TreeForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="children",
        help_text=_("Referral can have a hierarchy."),
    )
    code = models.CharField(
        max_length=64,
        verbose_name=_("code"),
        help_text=_("Referral code"),
    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        ordering = ["user"]
        verbose_name = _("referral")
        verbose_name_plural = _("referrals")
        permissions = (
            ("import_referral", _("Can import Referral")),
            ("export_referral", _("Can export Referral")),
        )

    def __str__(self):
        return str(self.user)

    @property
    def opts(self):
        return self.__class__._meta

    def clean(self):
        if self.parent:
            parent = self.parent
            if self.parent == self:
                raise ValidationError("Referral parent cannot be self.")
            if parent.parent and parent.parent == self:
                raise ValidationError("Cannot have circular parents.")

    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
