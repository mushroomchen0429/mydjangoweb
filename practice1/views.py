from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostModelForm


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

def new(request):
    # if request.method == 'POST':
    #     _title = request.POST.get('title')
    #     _content = request.POST.get('content')
    #
    #     if _title == '' or _content == '':
    #         return render(request, 'post/new.html',{
    #             'error' : ['有欄位未輸入']
    #         })
    #
    #     Post.objects.create(title = _title, content = _content)
    #     return redirect('posts_index')
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('posts_index')

    return render(request, 'post/new.html',{
        'form' : form
    })

def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostModelForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('posts_index')

    return render(request, 'post/edit.html', {
        'form': form
    })

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('posts_index')

