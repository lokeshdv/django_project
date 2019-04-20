from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'lokesh',
        'title':'kalu',
        'content':'FIRST POST OF MY PAGE ',
        'date_posted':'april 14 2019',
    },
        
    {
        'author':'paglu',
        'title':'pagla shubham',
        'content':'SECOND POST OF PAGLA ',
        'date_posted':'april 14 2019',
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render (request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'about'})

