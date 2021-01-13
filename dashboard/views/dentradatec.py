from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import DEntradaTec
from dashboard.forms.dentradatec_form import DEntradaTecRegisterForm


def dentradatec_list(request):
    datos = DEntradaTec.objects.all()
    return render(request, 'dashboard/dentradatec_list.html', {'datos': datos})


def dentradatec_register(request):
    if request.method == 'POST':
        form = DEntradaTecRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:meta_matriz_list')
        else:
            return render(request, 'dashboard/dentradatec_register.html', {'form': form})
    else:
        form = DEntradaTecRegisterForm()
        return render(request, 'dashboard/dentradatec_register.html', {'form': form})


def dentradatec_edit(request, id):
    form = None
    error = None
    try:
        dentradatec = DEntradaTec.objects.get(id = id)
        if request.method == 'GET':
            form = DEntradaTecRegisterForm(instance = dentradatec)
        else:
            form = DEntradaTecRegisterForm(request.POST, instance = dentradatec)
            if form.is_valid():
                form.save()
                return redirect('dashboard:dentradatec_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/dentradatec_register.html', {'form': form, 'error': error})
