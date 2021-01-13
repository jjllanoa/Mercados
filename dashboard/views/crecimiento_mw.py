from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import CrecimientoMW
from dashboard.forms.crecimiento_mw_form import CrecimientoMWRegisterForm


def crecimiento_mw_list(request):
    datos = CrecimientoMW.objects.all()
    return render(request, 'dashboard/crecimiento_mw_list.html', {'datos': datos})


def crecimiento_mw_register(request):
    if request.method == 'POST':
        form = CrecimientoMWRegisterForm(request.POST)
        if form.is_valid():
            # form.save()
            return redirect('dashboard:crecimiento_mw_list')
        else:
            return render(request, 'dashboard/crecimiento_mw_register.html', {'form': form})
    else:
        form = CrecimientoMWRegisterForm()
        return render(request, 'dashboard/crecimiento_mw_register.html', {'form': form})


def crecimiento_mw_edit(request, id):
    form = None
    error = None
    try:
        crecimiento_mw = CrecimientoMW.objects.get(id = id)
        if request.method == 'GET':
            form = CrecimientoMWRegisterForm(instance = crecimiento_mw)
        else:
            form = CrecimientoMWRegisterForm(request.POST, instance = crecimiento_mw)
            if form.is_valid():
                # form.save()
                return redirect('dashboard:crecimiento_mw_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/crecimiento_mw_register.html', {'form': form, 'error': error})
