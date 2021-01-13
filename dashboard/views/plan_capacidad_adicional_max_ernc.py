from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import PlanCapacidadAdicionalMaxERNC
from dashboard.forms.plan_capacidad_adicional_max_ernc_form import PlanCapacidadAdicionalMaxERNCRegisterForm


def plan_capacidad_adicional_max_ernc_list(request):
    datos = PlanCapacidadAdicionalMaxERNC.objects.all()
    return render(request, 'dashboard/plan_capacidad_adicional_max_ernc_list.html', {'datos': datos})


def plan_capacidad_adicional_max_ernc_register(request):
    if request.method == 'POST':
        form = PlanCapacidadAdicionalMaxERNCRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:plan_capacidad_adicional_max_ernc_list')
        else:
            return render(request, 'dashboard/plan_capacidad_adicional_max_ernc_register.html', {'form': form})
    else:
        form = PlanCapacidadAdicionalMaxERNCRegisterForm()
        return render(request, 'dashboard/plan_capacidad_adicional_max_ernc_register.html', {'form': form})


def plan_capacidad_adicional_max_ernc_edit(request, id):
    form = None
    error = None
    try:
        plan_capacidad_adicional_max_ernc = PlanCapacidadAdicionalMaxERNC.objects.get(id = id)
        if request.method == 'GET':
            form = PlanCapacidadAdicionalMaxERNCRegisterForm(instance = plan_capacidad_adicional_max_ernc)
        else:
            form = PlanCapacidadAdicionalMaxERNCRegisterForm(request.POST, instance = plan_capacidad_adicional_max_ernc)
            if form.is_valid():
                plan_capacidad_adicional_max_ernc.ernc = plan_capacidad_adicional_max_ernc.eolica + plan_capacidad_adicional_max_ernc.solar + plan_capacidad_adicional_max_ernc.pch + plan_capacidad_adicional_max_ernc.ndc_t
                form.save()
                return redirect('dashboard:plan_capacidad_adicional_max_ernc_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/plan_capacidad_adicional_max_ernc_register.html', {'form': form, 'error': error})
