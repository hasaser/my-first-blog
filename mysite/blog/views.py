from django.shortcuts import render,get_object_or_404, redirect, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.utils import timezone
from django.contrib import messages

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



# Create your views here.
