from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

def post_list(request):
    if request.method == "POST":
        if 'add_button' in request.POST:
            return redirect('post_new')
    posts = Post.objects.order_by('published_date')
    return render(request, 'todolist/post_list.html', {'posts' : posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'todolist/post_new.html', {'form' : form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    form = PostForm(instance=post)
    return render(request, 'todolist/post_edit.html', {'form' : form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')




