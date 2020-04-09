from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post

# Register your models here.
# admin.site.register(Post)
@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'content_size',
        'created_at', 
        'updated_at',
        '_type',
        )
    list_display_links = ['id', 'title']
    search_fields = ('title', )
    
    def content_size(self, post):
        return mark_safe('<u>{}</u>글자'.format(len(post.content)))
    content_size.short_description = '글자수'