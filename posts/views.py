from django.shortcuts import redirect, render
from . import models
from django.contrib import messages
# Create your views here.

def main(request):
    posts = models.Post.objects.all()[:10]
    featured_posts = models.Post.objects.filter(featured=True)[:5]
    latest_posts = models.Post.objects.all().order_by('-id')[:7]
    trending_posts = models.Post.objects.all().order_by('-views')[:7]
    trending_cats = models.Category.objects.all().order_by('-views')[:7]
    featured_cats = models.Category.objects.filter(featured=True).order_by('-views')[:7]
     
    messages.success(request, 'Successfully Created')
    ctx = {
        'featured_posts' : featured_posts,
        'featured_cats' : featured_cats,
        'latest_posts' : latest_posts,
        'trending_posts' : trending_posts,
        'trending_cats' : trending_cats,
        'posts' : posts,
    }
    return render(request,'index.html', ctx)

def blog(request):
    return render(request,'')

def post(request,id):
    post = models.Post.objects.get(id=id)
    latest_posts = models.Post.objects.all().order_by('-id')[:7]
    comment = models.Comment.objects.filter(post=post)
    ctx = {
        'post':post,
        'comment':comment,
        'latest_posts' : latest_posts,
    }
    return render(request,'post.html',ctx)

def author(request,id):
    author = models.Author.objects.get(id=id)
    posts = models.Post.objects.filter(author=author)
    ctx = {
        'author':author,
        'posts':posts
    }
    return render(request,'author.html',ctx)
def search(request):
    q = request.GET.get('q')
    if q is not None:
        posts = models.Post.objects.filter(title__icontains=q)
    else:
        posts = models.Post.objects.all()[:10]
    ctx = {
        'posts':posts
    }
    return render(request,'search.html',ctx)

def subscribe(request):
    email = request.GET.get('email')
    if email is not None:
        if models.Subscribe.objects.filter(email=email).exists():
            messages.error(request, 'alredy subscribed')
        else:
            models.Subscribe.objects.create(email=email)
            messages.success(request, 'subscribed')
    return redirect('main')
def comment(request,id):
    name = request.POST.get('name')
    email = request.POST.get('email')
    comment = request.POST.get('comment')
    post = models.Post.objects.get(id=id)
    models.Comment.objects.create(name=name ,email=email ,comment=comment ,post=post)
    return redirect(f'/post/{id}')