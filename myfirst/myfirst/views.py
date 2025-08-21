from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<h1 style="color:red">Hello!</h1>')

def home(request):
    return render(request, template_name='index.html')

def get_post(request):
    all_posts = Post.objects.all()
    return render(request, template_name='posts.html', context={"all_posts": all_posts})

def create_posts(request):
    return render(request, 'posts/post.html')