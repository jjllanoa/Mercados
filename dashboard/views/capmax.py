from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import CapMax
from dashboard.forms.capmax_form import CapMaxRegisterForm


def capmax_list(request):
    datos = CapMax.objects.all()
    return render(request, 'dashboard/capmax_list.html', {'datos': datos})


def capmax_register(request):
    if request.method == 'POST':
        form = CapMaxRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:capmax_list')
        else:
            return render(request, 'dashboard/capmax_register.html', {'form': form})
    else:
        form = CapMaxRegisterForm()
        return render(request, 'dashboard/capmax_register.html', {'form': form})


def capmax_edit(request, id):
    form = None
    error = None
    try:
        capmax = CapMax.objects.get(id = id)
        if request.method == 'GET':
            form = CapMaxRegisterForm(instance = capmax)
        else:
            form = CapMaxRegisterForm(request.POST, instance = capmax)
            if form.is_valid():
                form.save()
                return redirect('dashboard:capmax_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/capmax_register.html', {'form': form, 'error': error})
