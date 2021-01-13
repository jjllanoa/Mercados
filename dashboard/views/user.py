from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from dashboard.forms.user_form import UserRegisterForm, UserEditForm


def user_list(request):
    usuarios = User.objects.all()
    print(usuarios)
    return render(request, 'dashboard/user_list.html', {'usuarios': usuarios})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            is_active = form.cleaned_data.get('is_active')

            usuario = User(username=username, email=username, is_active=is_active)
            usuario.save()
            usuario.set_password(password)
            usuario.save()

            return redirect('dashboard:user_list')
        else:
            return render(request, 'dashboard/user_register.html', {'form': form})
    else:
        form = UserRegisterForm()
        return render(request, 'dashboard/user_register.html', {'form': form})


def user_edit(request, id):
    form = None
    error = None
    try:
        usuario = User.objects.get(id = id)
        datos = {'email': usuario.email}

        if request.method == 'GET':
            form = UserEditForm(initial=datos)
        else:
            form = UserEditForm(request.POST, initial=datos)

            if form.is_valid():
                username = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password1')
                is_active = form.cleaned_data.get('is_active')

                usuario.email = username
                # usuario.save()
                usuario.username = username
                # usuario.save()
                usuario.is_active = is_active
                # usuario.save()

                if (password is not None) or (password is not ''):
                    usuario.set_password(password)
                    # usuario.save()

                return redirect('dashboard:user_list')
            else:
                return render(request, 'dashboard/user_register.html', {'form': form})

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/user_register.html', {'form': form, 'error': error})


def user_delete(request, id):
    pass
