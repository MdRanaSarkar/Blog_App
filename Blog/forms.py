from django import forms
from .models import Author, Category, Article, Category, Author, Commentd
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class CreateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'body',
            'image',
            'category'
        ]


class Register_Form(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'

        ]


class AuthorForm(forms.ModelForm):
    class  Meta:
        model = Author
        fields = [
            'profile_pic',
            'details'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Commentd
        fields = [
            'name',
            'gmail',
            'commen'
        ]


class CatergoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = [
            'name'
        ]