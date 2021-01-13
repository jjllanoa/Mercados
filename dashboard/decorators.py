from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):

        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect('index')
            else:
                return redirect('dashboard:no_auth')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func