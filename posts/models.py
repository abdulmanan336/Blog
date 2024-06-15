from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Author(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    prof = models.CharField(max_length=250)
    info = models.TextField()
    crated_at = models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True)
    avatar = models.ImageField(upload_to='author/',blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
class Category(models.Model):
    title = models.CharField(max_length=250)
    views = models.PositiveSmallIntegerField(default=0)
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='cats/',blank=True, null=True)


    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/',blank=True, null=True)
    overview = models.TextField()
    content = RichTextField(null=True,blank=True)
    # content = models.TextField()
    featured = models.BooleanField(default=False)
    views = models.PositiveSmallIntegerField(default=0)
    shares = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at= models.DateField(auto_now=True)
    previous = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='postprevious', null=True)
    next = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='postnext',null=True)
    
    def __str__(self):
        return self.title

class Subscribe(models.Model):
    email = models.EmailField(max_length=254,unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email

class Comment(models.Model):
    post =models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=50 ,null=True)
    email = models.EmailField( max_length=254)
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
