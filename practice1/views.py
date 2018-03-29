from django.shortcuts import render, get_object_or_404
from .models import Post


def index(request):
    posts = Post.objects.all();
    return render(request, 'post/index.html',{
        'posts':posts,}
    )


def show(request, pk):
    # post = Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk = pk)
    return render(request, 'post/show.html',{
        'posts':post,
    })

def new():
    pass

def edit():
    pass

def delete():
    pass

