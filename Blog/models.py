from django.db import models
from django.shortcuts import reverse

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    profile_pic=models.FileField()
    details = models.TextField()
    def __str__(self):
        return self.details
class Category(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class Article(models.Model):
    article_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.TextField()
    image=models.FileField()
    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def get_single_url(self):
        return reverse('Blog:single', kwargs={'id': self.id})
        
    
class Amar(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    
class Commentd(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    gmail=models.EmailField(max_length=254)
    commen = models.TextField()
    
    def __str__(self):
        return self.post.title

    
    
    
