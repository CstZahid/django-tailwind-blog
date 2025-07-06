from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost

def home(request):
    posts = BlogPost.objects.order_by('-created_at')
    return render(request, 'home.html', {'posts': posts})

def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        author = request.POST['author']
        image = request.FILES.get('image')

        BlogPost.objects.create(title=title, content=content, author=author, image=image)
        return redirect('home')
    return render(request, 'create_post.html')

def view_post(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    return render(request, 'view_post.html', {'post': post})
