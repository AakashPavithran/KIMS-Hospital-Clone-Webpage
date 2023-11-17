from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from .models import Doctor
from .models import Medicine

# Create your views here.

def demo(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def department(request):
    return render(request, "department.html")

def doctor(request):
    obj=Doctor.objects.all()
    return render(request, "doctor.html" ,{'result': obj})

def medicine(request):
    obj=Medicine.objects.all()
    return render(request, "medicine.html",{'result': obj})

def booking(request):
    return render(request, "booking.html")

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect("login")
    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email Taken")
                return redirect ("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect("register")
            else:
                user=User.objects.create_user(email=email,username=username,password=password)




                user.save() 
                return redirect('login')
            # print("user created")
        else:
            messages.info(request,"password not matching")
            return redirect("register")

        return redirect('/')

    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')
    