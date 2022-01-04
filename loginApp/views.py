from django.shortcuts import render , redirect
from .forms import UserRegisterForm , UserLoginForm , UserProfilForm
from django.contrib.auth import login
from blog.models import MyUser , Comment ,Blog
from taggit.models import Tag
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView

# Create your views here.

def user_login(request):
    if request.method =="POST":
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog')
    else :
        form = UserLoginForm()
    return render(request, 'login.html',{'form':form})

def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, 'signup.html',{'form':form})

@login_required(login_url='login')
def user_update(request, slug_name):
    user = MyUser.objects.get(username=slug_name)
    if request.method == 'POST':
        form = UserProfilForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profil', slug_name=user.username)
    else:
        form = UserProfilForm(instance=user)
    return render(request, 'profil.html', {'form': form,'user':user})

def userprofile(request, slug_name):
    user = MyUser.objects.get(username=slug_name)
    blogs = Blog.objects.filter(user_id__username = slug_name)
    tag = Tag.objects.all().order_by('name')[:4]
    cnt = Tag.objects.all().count()
    if cnt > 4 :
        tags = Tag.objects.all().order_by('-name')[:(cnt-4)]
    comments = Comment.objects.filter(user_id__username = slug_name)
    top = Blog.objects.all().order_by('-views')[:5]
    post = Blog.objects.all().order_by('-views')[:5]
    return render(request, 'user_profil.html', {'users':user,'blogs':blogs,'comments':comments,'tag':tag,'tags':tags,'cnt':cnt,'post':post})
