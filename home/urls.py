from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
     
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name='about'),
    path('search/',views.search,name='search'),
    path('login',views.handlelogin,name='handlelogin'),
    path('signup',views.handlesignup,name='handlesignup'),
    path('logOut',views.handlelogOut,name='handlelogOut'),
       
]