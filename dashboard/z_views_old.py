from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='dashboard:login')
def Index(request):
    return render(request, 'dashboard/index.html')


def Register(request):
    return render(request, 'dashboard/auth/register.html')
    # if request.user.is_authenticated:
    #     return redirect('/')
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password1')
    #         user = authenticate(username=username, password=password)
    #         login(request, user)
    #         return redirect('/')
    #     else:
    #         return render(request, 'dashboard/auth/register.html', {'form': form})
    # else:
    #     form = UserCreationForm()
    #     return render(request, 'dashboard/auth/register.html', {'form': form})


def Login(request):
    # return render(request, 'dashboard/auth/login.html')
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Three credits remain in your account.')
            form = AuthenticationForm(request.POST)
            return render(request, 'dashboard/auth/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'dashboard/auth/login.html', {'form': form})


def Logout(request):
    logout(request)
    return redirect('/')


def ListUsers(request):
    # usuario = Usuario.objects.filter(estado=True)
    usuario = None
    return render(request, 'dashboard/list_users.html', {'usuario': usuario})