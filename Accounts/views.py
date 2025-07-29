from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import SignUpForm
from .models import SignUpModel
from django.contrib import messages


def signUp(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        uname = form.cleaned_data['username']
        email = form.cleaned_data['email']
        pin = form.cleaned_data['pin']
        confirm_pin=request.POST.get("confirm_pin")
        if confirm_pin!=pin:   
                messages.error(request, "Pin not matched")
                return render(request, 'Accounts/signUpPage.html', {'form': form})
        if not User.objects.filter(username=uname).exists() :
                                user = User.objects.create_user(username=uname, email=email, password=pin)
                                account=  SignUpModel.objects.create(user=user, email=email, pin=pin)
                                account.save()
                                messages.success(request, "Account created successfully!")
                                return redirect('login')
        else:
                            messages.error(request, "Account already exitsts")
                            return render(request, 'Accounts/signUpPage.html', {'form': form})       
    return render(request, 'Accounts/signUpPage.html', {'form': form})






def login(request):
    if request.method == 'POST':
            uname = request.POST.get('username')
            pin = request.POST.get('pin')
            user = authenticate(request, username=uname, password=pin)
            if  SignUpModel.objects.filter(user=user).exists():
                auth_login(request, user)
                messages.success(request, "Login successful!")
                return redirect('show') 
            else:
               messages.error(request,"Invalid Username or pin") 
               return redirect('login')
    return render(request, 'accounts/loginPage.html')






def logout(request):
    auth_logout(request)
    messages.info(request,"Logged Out!")
    return redirect('login')