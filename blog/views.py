from django.shortcuts import render
from .models import BlogPost
from datetime import date



def index(request):
    myposts =BlogPost.objects.all()
    print(myposts)
    return render(request, 'blog/index.html',{'myposts':myposts})


def blogpost(request, id):
    post = BlogPost.objects.filter(post_id=id)[0]
    today = date.today()
    d2 = today.strftime("%B %d, %Y")
    return render(request, 'blog/blogpost.html',{'post':post,'d2':d2})
