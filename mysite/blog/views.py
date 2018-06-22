from django.shortcuts import render,get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.contrib import messages
from django.urls import reverse

def post_düzenle(request,id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "Başarılı bir şekilde güncellediniz.",'alert alert-success')
        return HttpResponseRedirect(post.get_absolute_url())
    return render(request,"blog/yeni_post.html",{ "form":form })

def yeni_post(request):
    form = PostForm(request.POST or None)
    if(form.is_valid()):
        post = form.save()
        messages.success(request,"Başarılı bir şekilde oluşturdunuz.")
        return HttpResponseRedirect(post.get_absolute_url())
    return render(request,"blog/yeni_post.html",{"form":form})

def sil(request,id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect("anasayfa")

def anasayfa(request):
    posts= list(reversed(Post.objects.all()))
    return render(request,"blog/anasayfa.html",{"posts":posts})

def icerik(request,id):
    post=get_object_or_404(Post,id=id)
    return render(request,"blog/icerik.html",{"post":post})

def giris(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('anasayfa'))
        else:
            raise request.ValidationError("Şifre veya kullanıcı adı yanlış!")
    return render(request,"blog/log_in.html",{"form":form,"urlsi":reverse("kayit")})

def kayit(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('example:log_in'))
        else:
            print(form.errors)
    return render(request,"blog/kayıt.html",{"form":form,"urlsi":reverse("giris")})

def cıkıs(request):
    logout(request)
    return redirect(reverse("giris"))
# Create your views here.
