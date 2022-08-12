
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse

from django.contrib.auth.models import User
from .forms import UserForm, UserRegistration

from django import forms


def signin(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = UserForm()
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        username = email.split('@')[0]
        user = authenticate(request, username=username, password=password)

        if user is None:
            return render(request, 'auth/login.html', {'form': form, 'error_message': 'Incorrect login credentials'})

        login(request, user)
        return redirect('/')
    else:
        return render(request, 'auth/login.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('login')


def check_username(username):
    try:
        email_check = User.objects.get(username=username)
    except User.DoesNotExist:
        return username
    raise forms.ValidationError("Username already exists")


def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    form = UserRegistration()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = email.split('@')[0]
        confirm_password = request.POST['confirm-password']

        if len(password) < 6:
            return render(request, 'auth/register.html', {'form': form, 'error_message': 'Password min length is 6'})

        if password != confirm_password:
            return render(request, 'auth/register.html', {'form': form, 'error_message': 'Password does not match'})

        try:
            check_username(username)

            newuser = User.objects.create_user(
                email=email, password=password, username=username)
            newuser.save()
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('/')
        except forms.ValidationError:
            return render(request, 'auth/register.html', {'form': form, 'error_message': 'Email already exists.'})
        except:
            return render(request, 'auth/register.html', {'form': form, 'error_message': 'Something went wrong.'})

    return render(request, 'auth/register.html', {'form': form})
