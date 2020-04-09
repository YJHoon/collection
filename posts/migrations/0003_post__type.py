# Generated by Django 3.0.4 on 2020-03-19 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200319_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='_type',
            field=models.PositiveSmallIntegerField(choices=[(0, '칼럼'), (1, '뉴스'), (2, '소설')], default=0, verbose_name='게시글 타입'),
            preserve_default=False,
        ),
    ]
