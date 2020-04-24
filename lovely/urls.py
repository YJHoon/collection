from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import main, new, create, delete

app_name = "lovely"
urlpatterns = [
  path('', main, name="main"),
  path('new/', new, name="new"),
  path('create/', create, name="create"),
  path('delete/', delete, name="delete"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)