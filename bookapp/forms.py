import django.utils.crypto
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from bookapp.models import Books


class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:

        model=User
        fields=["first_name","last_name","username","email","password1","password2"]
        widgets={
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"})

        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

class BookForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=["book_name","price","author_name","publisher","qty"]
        widgets={
            "book_name":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.TextInput(attrs={"class":"form-control"}),
            "author_name":forms.TextInput(attrs={"class":"form-control"}),
            "publisher":forms.TextInput(attrs={"class":"form-control"}),
            "qty":forms.TextInput(attrs={"class":"form-control"})
        }

class BookChangeForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=[
            "book_name","price","author_name","publisher","qty"
        ]

