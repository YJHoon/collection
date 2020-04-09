from django.db import models
from django.urls import reverse

class Post(models.Model):
    class Meta:
        ordering = ['-created_at']

    POST_TYPES = [
        (0, "칼럼"),
        (1, "뉴스"),
        (2, "소설"),
    ]
    title = models.CharField(max_length=10,
                             verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    view_count = models.IntegerField(default=0,
                                    verbose_name="조회수")
    _type = models.PositiveSmallIntegerField(choices=POST_TYPES,
                                      verbose_name="게시글 타입")
    image = models.ImageField(upload_to='posts/img', default="posts/default/dgu.png")

    created_at = models.DateTimeField(auto_now_add = True,
                                      verbose_name="등록 시간")
    updated_at = models.DateTimeField(auto_now = True,
                                      verbose_name="업데이트 시간")
# Create your models here.


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:show", args=[self.pk])
    