from ast import Param
import email
from importlib.resources import contents
from turtle import title
from unicodedata import name
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib.messages import constants as messages
from django.contrib.auth import authenticate, login, logout
import os
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User


# Create your views here.
# HTML pages render here
def home(request):
    # return HttpResponse("This is Home.....")
    return render(request, 'home/home.html')


def contact(request):
    # return HttpResponse("This is a Contact......")
    # messages.error(request, "Your message has been successfully sent")
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        # print(name,email,phone,content)
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "please fill the form correctly.")
        else:
            contact = Contact(name=name, email=email,
                              phone=phone, content=content)
            contact.save()
            messages.success(request, "Your from is submit successfully..")
    return render(request, 'home/contact.html')


def about(request):

    # return HttpResponse("This is a About....")

    return render(request,'home/about.html')


def search(request):

    query = request.GET['query']
    if len(query) > 78:
        allPosts == Post.objects.none()
    else:
        # allPosts =Post.objects.all()
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count() == 0:
        messages.warning(
            request, "Bo search results found. Please refine your query.. ")
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)
    # return HttpResponse("This is search")

# Authetication APIs
def handlesignup(request):
    if request.method == 'POST':
        # Get the post parameter
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Cheks for errorneous inputs

        if len(username) > 10:
            messages.error(request, "username must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(
                request, "username should only contain letters and numbers")
            return redirect('home')

        if pass1 != pass2:
            messages.error(
                request, "Your Passward is do not match! Enter the same passward...")
            return redirect('home')
        if not fname.isalpha() and not lname.isalpha():
            messages.error(
                request, "First name or Last name  should only contain letters ")
            return redirect('home')

        # create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(
            request, "Your myBlog account has been successfully created")
        return redirect('home')

    else:
        return HttpResponse('404 - Not Found')


def handlelogin(request):
    if request.method == 'POST':
        # Get the post parameter

        loginusername = request.POST['loginusername']
        loginpassward = request.POST['loginpassward']

        user = authenticate(username=loginusername, password=loginpassward)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Loged In")
            return redirect('home')

        else:
            messages.error(request, "Invalid Username or Password")
            return redirect('home')
    return HttpResponse('404 - Not Found')


def handlelogOut(request):

    logout(request)
    messages.success(request, "Successfully Logged Out In")
    return redirect('home')
    # return HttpResponse('handlelogOut')
