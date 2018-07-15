from django.shortcuts import render
from .models import Posts

# Create your views here.
def allposts(request):
    posts=Posts.objects
    return render(request,'posts/allposts.html',{'posts':posts})
