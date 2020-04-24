from django.db import models
from django.urls import reverse
from users.models import User
from django.utils.translation import ugettext_lazy as _
from templates.shared.timestamped import TimeStampedModel


class Post(TimeStampedModel):
    class Meta:
        ordering = ['-created_at']

    POST_TYPES = [
        (0, "칼럼"),
        (1, "뉴스"),
        (2, "소설"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="사용자")
    title = models.CharField(_("제목"), max_length=50)
    content = models.TextField(_("내용"))
    view_count = models.IntegerField(_("조회수"), default=0)
    _type = models.PositiveSmallIntegerField(_("게시글 타입"), choices=POST_TYPES)
    image = models.ImageField(_("게시글"), upload_to='posts/img', default="posts/default/dgu.png")


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:show", args=[self.pk])
    