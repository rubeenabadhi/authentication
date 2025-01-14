from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect

def home(request):
    return render(request,'index.html')
def register(request):
    if request.method=="POST":
        first_name= request.POST["first_name"]
        last_name= request.POST["last_name"]
        username= request.POST["username"]
        password1= request.POST["password1"]
        password2= request.POST["password2"]
        email= request.POST["email"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username is already taken')
                return redirect("/")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is already taken")
                return redirect("/")
            else:
                user= User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()

        else:
            print("password not correct")
            messages.info(request, "passwords are not equel")
            return redirect("/")
        return redirect("/")
    else:
        return render(request,"register.html")
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password= request.POST['password']
        user= auth.authenticate(username=username,password=password)
        print(user)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid details')
            return redirect('login')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

# Create your views here.
