from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def log_in(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'El usuario no es válido.')
            form = AuthenticationForm(request.POST)
            return render(request, 'dashboard/auth/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'dashboard/auth/login.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect('dashboard:login')
