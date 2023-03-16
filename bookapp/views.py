from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,ListView,UpdateView,DetailView
from django.contrib.auth.models import User
from bookapp import forms
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from bookapp.models import Books

# Create your views here.


class SignUpView(CreateView):
    model= User
    form_class = forms.RegistrationForm
    template_name = "registration.html"
    success_url =reverse_lazy("signin")



class LoginView(View ):
    def get(self,request,*args,**kwargs):
        form=forms.LoginForm()
        return render(request,"login.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=forms.LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                print("login success")
                return redirect("index")
            else:
                print("login failed")
                return render(request,"login.html",{"form":form})

class IndexView(TemplateView):
    template_name = "home.html"


class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")

class BookAddView(CreateView):
    model=Books
    form_class = forms.BookForm
    template_name = "add-Book.html"
    success_url = reverse_lazy("books-list")

    # def form_valid(self, form):
    #     form.instance.user=self.request.user
    #     # messages.success(self.request,"book has been added")
    #     return super().form_valid(form)


class BookListView(ListView):
    model = Books
    context_object_name = "books"
    template_name = "booklist.html"

    # def get_queryset(self):
    #     return Books.objects.filter(user=self.request.user)

def delete_books(request,*args,**kwargs):
    id=kwargs.get("id")
    Books.objects.get(id=id).delete()
    return redirect("books-list")

class BookDetailView(DetailView):
    model = Books
    context_object_name = "book"
    template_name = "book-detail.html"
    pk_url_kwarg = "id"

class BookEditView(UpdateView):
    model = Books
    form_class =forms.BookChangeForm
    template_name = "book_edit.html"
    success_url = reverse_lazy("books-list")
    pk_url_kwarg = "id"






