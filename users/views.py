from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            login(request,new_user)
            return redirect("library:list")
    else:
        form = UserCreationForm()#form is a reternd info
    return render(request,'register.html',{"form": form})
@csrf_exempt
def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect("library:list")
    else:
         form=AuthenticationForm()
    return render(request,'login.html',{"form" :form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")