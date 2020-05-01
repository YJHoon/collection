from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Lovely
import pdb

def main(request):
  context = {
    'lovely': Lovely.objects.all()
  }
  return render(request, 'lovely/main.html', context)


@login_required(login_url= '/accounts/login')
def new(request):
  return render(request, 'lovely/new.html')


@login_required(login_url= '/accounts/login')
def create(request):
  if request.method == "POST":
    image = request.FILES.get('image')
    # Lovely(image = image).save()
    Lovely.objects.create(image = image)
    return redirect('lovely:main')


@login_required(login_url= '/accounts/login')
def delete(request):
  return redirect('main')