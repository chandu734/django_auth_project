from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User


def indexView(request):
    return render(request,'index.html')

@login_required(login_url='/login')
def aboutView(request):
    # print(request.user.is_authenticated)
    return render(request,'about.html')

def signupView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email)
        if user:
            messages.error(request,f'{email} Already Taken!!!')
            return redirect('signup')
        new_user = User(username=username,email=email)
        new_user.set_password(password)
        new_user.save()
        return redirect('/login')
    return render(request,'signup.html')

def loginView(request):
    if request.user.is_authenticated:
        return redirect('about')
        
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials')
            return render(request,'login.html')
    return render(request,'login.html')

def logoutView(request):
    logout(request)
    return redirect('login')