from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import main, new, create, show, edit, update, delete


app_name = 'posts'
urlpatterns = [
  path('', main, name="main"),
  path('new/', new, name="new"),
  path('create/', create, name="create"),
  path('<int:post_id>/', show, name="show"),
  path('edit/<int:post_id>/', edit, name="edit"),
  path('update/<int:post_id>/', update, name="update"),
  path('delete/<int:post_id>/', delete, name="delete"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)