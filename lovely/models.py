from django.db import models
from templates.shared.timestamped import TimeStampedModel
from django.utils.translation import ugettext_lazy as _

class Lovely(TimeStampedModel):
  image = models.ImageField(_("이미지"), upload_to="lovely/img/", default="lovely/default/photo.png", null=False)