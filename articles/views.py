from multiprocessing import context
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.forms import  *
from django.contrib.auth import  login, logout,authenticate
from .models import Profile
from django.contrib.auth.models import User

def register_view(request):
    formset=NewProfile(request.POST, request.FILES)
    form =form=UserCreationForm(request.POST or None)
    if request.method =='POST':
        if all([form.is_valid(), formset.is_valid()]):
            
            usr_obj = form.save()
            profile_obj=formset.save()
            return redirect('/')
    else:
        formset= NewProfile()
        form=UserCreationForm()
    context={
        'form': form,
        'formset': formset,

    }    
    return render(request,'register.html',context)



def delete(request, id):
    obj= Profile.objects.get(id=id)
    

    obj.delete()
    return redirect('/')

def edit(request,id):
  obj= Profile.objects.get(id=id)

  form=NewProfile(request.POST or None ,instance=obj)
  if form.is_valid():
         
         form.save()
         
         return redirect('/')
  
        
  return render(request,'edit.html',{'form': form,})

def display(request, id):
    obj= Profile.objects.get(id=id)
    context={ "obj": obj,
        " name": obj.name,
        "username":obj.id2,
     "id":obj.id,
     "age": obj.age,
     "occupation":obj.occupation,
     "place": obj.place,
     "joining_date":obj.joining_date,
     "email-id":obj.email_id}
    return render(request,'display.html',context)

def login_view(request):
    if request.method=="POST":
       username = request.POST.get("username")
       password =request.POST.get("password")
       user = authenticate(request,username=username,
       password=password)
       if user is None:
           context={"error":"Invalid Username or Password"}
           return render(request, "accounts/login.html",
           context)
       login(request,user)
       return redirect('/')
    return render(request, "accounts/login.html")
    

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html",{})