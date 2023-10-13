from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Student
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

def index(request):
    data = Student.objects.all()
    context={"data":data}
    return render(request,"index.html",context)

def about(request):
    return render(request,"about.html")

def insertData(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        query = Student(name=name,email=email,age=age,gender=gender)
        query.save()
        return redirect("/")
    return render(request,"index.html")

def updateData(request,id):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']

        edit = Student.objects.get(id=id)
        edit.name = name
        edit.email = email
        edit.age = age
        edit.gender = gender
        edit.save()
         
        return redirect("/")
    d = Student.objects.get(id=id)
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username")
            return redirect("/login")
        
        user = authenticate(username = username , password = password)

        if user is None:
            messages.info(request, "Invalid Password")
            return redirect("/login")
        
        else:
            login(request, user)
            return redirect("/")
            

    return render(request,"login.html")


def logout_page(request):
    logout(request)
    return redirect("/login")

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already taken")
            return redirect("/register")
    
        user = User.objects.create(first_name=first_name,last_name=last_name,username=username)
        user.set_password(password)
        user.save()

        messages.info(request, "Account created succesfully")
        return redirect("/register")

    return render(request,"register.html")