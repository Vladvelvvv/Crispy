from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from users.forms import ProfileForm, UserLoginForm, UserRegistrationForm

@login_required
def profile(request):
    
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Данные профиля успешно обновлены')
            return redirect(reverse('users:profile'))
    else:
        form = ProfileForm(instance=request.user)
    
    context = {
        'title': 'Профиль',
        'class': 'profile',
        'form' : form,
    }
    
    return render(request, "users/profile.html", context=context)

def login(request):
    
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                messages.success(request, f"{username}, Вы успешно зашли в аккаунт!")
                
                redirect_page = request.POST.get('next', None)
                if redirect_page and redirect_page != reverse('user:logout'):
                    return HttpResponseRedirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()
    
    context = {
        'title': 'Вход',
        'class': 'profile',
        'form' : form,
    }
    
    return render(request, "users/login.html", context=context)

@login_required
def logout(request):
    
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))

def registration(request):
    
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            messages.success(request, f"{user.username}, Вы успешно зарегистрировались и зашли в аккаунт!")
            return  redirect(reverse('users:profile'))
    else:
        form = UserRegistrationForm()
    
    context = {
        'title': 'Регистрация',
        'class': 'profile',
        'form' : form,
    }
    
    return render(request, "users/registration.html", context=context)
    

def forget_password(request):
    
    context = {
        'title': 'Восстановление пароля',
        'class': 'profile',
    }
    
    return render(request, "users/forget-password.html", context=context)

def new_password(request):
    
    context = {
        'title': 'Восстановление пароля',
        'class': 'profile',
    }
    
    return render(request, "users/new-password.html", context=context)

