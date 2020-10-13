from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']

        user=auth.authenticate(email=email,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('')
        else:
             return redirect('register')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=='POST':
        # first_name=request.POST['first_name']
        username=request.POST['name']
        password1=request.POST['password']
        # password2=request.POST['password2']
        email=request.POST['email']

        user=User.objects.create_user(username=username,password=password1,email=email)
        user.save()
        print('user created')
        return redirect('/')


    else:
        return render(request,'register.html')
