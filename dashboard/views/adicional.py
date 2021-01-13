from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import Adicional
from dashboard.forms.adicional_form import AdicionalRegisterForm


def adicional_list(request):
    datos = Adicional.objects.all()
    return render(request, 'dashboard/adicional_list.html', {'datos': datos})


def adicional_register(request):
    if request.method == 'POST':
        form = AdicionalRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:adicional_list')
        else:
            return render(request, 'dashboard/adicional_register.html', {'form': form})
    else:
        form = AdicionalRegisterForm()
        return render(request, 'dashboard/adicional_register.html', {'form': form})


def adicional_edit(request, id):
    form = None
    error = None
    try:
        adicional = Adicional.objects.get(id = id)
        if request.method == 'GET':
            form = AdicionalRegisterForm(instance = adicional)
        else:
            form = AdicionalRegisterForm(request.POST, instance = adicional)
            if form.is_valid():
                form.save()
                return redirect('dashboard:adicional_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/adicional_register.html', {'form': form, 'error': error})
