from django.shortcuts import render,get_object_or_404
from .models import Posts

# Create your views here.
def allposts(request):
    posts=Posts.objects
    return render(request,'posts/allposts.html',{'posts':posts})
def detail(request,posts_id):
    po=get_object_or_404(Posts,pk=posts_id)
    return render(request,'posts/detail.html',{'post':po})
