from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import ConsolidadoExistente
from dashboard.forms.consolidado_existente_form import ConsolidadoExistenteRegisterForm


def consolidado_existente_list(request):
    datos = ConsolidadoExistente.objects.all()
    return render(request, 'dashboard/consolidado_existente_list.html', {'datos': datos})


def consolidado_existente_register(request):
    if request.method == 'POST':
        form = ConsolidadoExistenteRegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            return redirect('dashboard:consolidado_existente_list')
        else:
            return render(request, 'dashboard/consolidado_existente_register.html', {'form': form})
    else:
        form = ConsolidadoExistenteRegisterForm()
        return render(request, 'dashboard/consolidado_existente_register.html', {'form': form})


def consolidado_existente_edit(request, id):
    form = None
    error = None
    try:
        consolidado_existente = ConsolidadoExistente.objects.get(id = id)
        if request.method == 'GET':
            form = ConsolidadoExistenteRegisterForm(instance = consolidado_existente)
        else:
            form = ConsolidadoExistenteRegisterForm(request.POST, instance = consolidado_existente)
            if form.is_valid():
                # form.save()
                return redirect('dashboard:consolidado_existente_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/consolidado_existente_register.html', {'form': form, 'error': error})
