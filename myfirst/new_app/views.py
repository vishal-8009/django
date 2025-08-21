from django.shortcuts import render

from django.http import HttpResponse

from new_app.models import Posts

# Create your views here.

def new_app(request):
    return render(request, 'new_app/index.html')



def get_posts(request):
    allposts =  Posts.objects.all()
    return render(request,'new_app/posts.html', context={"all_posts": allposts})



def create_post(request):
    return render(request, 'new_app/new_post.html')
