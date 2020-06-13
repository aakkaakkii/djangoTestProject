from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from post.forms import PostForm
from post.models import Post


def index(request):
    post_list = Post.objects.all()
    context = {
        'post_list': post_list
    }
    return render(request, 'index.html', context)


def create_post(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))

    context = {
        'form': form
    }
    return render(request, 'create_post.html', context)


def post(request, post_id):
    post_instance = get_object_or_404(Post, id=post_id)
    context = {
        'post': post_instance
    }
    return render(request, 'post.html', context)
