from django import forms
from .models import Lovely

class LovelyForm(forms.ModelForm):
  class Meta:
    model = Lovely
    fields = ['image']
    labels = {
      'image': '사진',
    }