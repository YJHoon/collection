from django.db import models
from django.contrib.auth.models import AbstractUser
from templates.shared.timestamped import TimeStampedModel
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser, TimeStampedModel):
  image = models.ImageField(_("프로필사진"), upload_to="users/img", default="users/default/photo.png")
  info = models.CharField(_("소개"), max_length=200, blank=True)