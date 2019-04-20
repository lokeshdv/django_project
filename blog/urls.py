from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='blog-home'),
    path('blog_about',views.about,name='blog_about') 
]