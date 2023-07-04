from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import Singup, loginForm,PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Post
from django.contrib.auth.models import Group


def home(request):
    posts = Post.objects.all()
    return render(request, 'Blog/Home.html', {'form': posts})


def about(request):
    return render(request, 'Blog/About.html')


def contact(request):
    return render(request, 'Blog/contact.html')


def dashboard(request):
    if request.user.is_authenticated:
        posts = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request, 'Blog/dashboard.html',{'Post':posts,'full_name':full_name,'Groups':gps})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


def user_singup(request):
    if request.method == 'POST':
        form = Singup(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name = 'Author')
            user.groups.add(group)
            messages.success(request, 'Congrationals!! You have become an Author!!')
            return HttpResponseRedirect('/Singup/')
    else:
        form = Singup()
    return render(request, 'Blog/Singup.html', {'fm': form})


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = loginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data.get('username')
                upass = form.cleaned_data.get('password')
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = loginForm()
        return render(request, 'Blog/login.html', {'fm': form})
    else:
        return HttpResponseRedirect('/dashboard /')


def Aadmin(request):
    return HttpResponseRedirect('/admin')

# Add New Post

def Add_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                desc = form.cleaned_data.get('desc')
                pst = Post(title=title,desc=desc)
                pst.save()
                messages.success(request,'Blog has been Created !!')
                return HttpResponseRedirect('/addpost/')
        else:
            form = PostForm()
        return render(request,'Blog/Addpost.html',{'fm':form})
    else:
        return HttpResponseRedirect('/login/')
    
#Update Existing Post

def update_post(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            form = PostForm(request.POST,instance=pi)
            if form.is_valid():
                form.save()
                messages.success(request,'Blog Updated!!')
        else:
            pi = Post.objects.get(pk=id)
            form = PostForm(instance=pi)
        return render(request,'Blog/Updatepost.html',{'fm':form})
    else:
        return HttpResponseRedirect('/login/')
    
#Delete Existing Post

def delete_post(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')
    

