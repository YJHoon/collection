from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
import pdb
from django.views.decorators.http import require_POST


# Create your views here.
def main(request):
  context = {
    'posts': Post.objects.all()
  }
  return render(request, 'posts/main.html', context)


def new(request):
  context = {
    'form': PostForm()
  }
  return render(request, 'posts/new.html', context)


@require_POST
def create(request):
  form = PostForm(request.POST, request.FILES or None)
  if form.is_valid():
    form.save()
  return redirect(form.instance)


def show(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  default_view_count = post.view_count
  post.view_count = default_view_count + 1
  post.save()
  context = {
    'post': post
  }
  return render(request, 'posts/show.html', context)


def edit(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  context = {
    'post': post,
    'form': PostForm(instance=post)
  }
  return render(request, 'posts/edit.html', context)


@require_POST
def update(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  # pdb.set_trace()
  form = PostForm(request.POST, request.FILES or None, instance=post) # 그냥 작성하면 create를 해버리기 때문에 instance를 정의해줘서 찾은 post를 이용한다고 명시해줘야 한다.
  # form.save를 하면 새로운 객체를 생성하지만 instance를 적어주면 update해준다라고 알면 될 듯
  if form.is_valid():
    form.save()
  return redirect(post)
    

@require_POST
def delete(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  post.delete()
  return redirect('main')