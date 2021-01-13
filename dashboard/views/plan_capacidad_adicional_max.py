from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import PlanCapacidadAdicionalMax
from dashboard.forms.plan_capacidad_adicional_max_form import PlanCapacidadAdicionalMaxRegisterForm


def plan_capacidad_adicional_max_list(request):
    datos = PlanCapacidadAdicionalMax.objects.all()
    return render(request, 'dashboard/plan_capacidad_adicional_max_list.html', {'datos': datos})


def plan_capacidad_adicional_max_register(request):
    if request.method == 'POST':
        form = PlanCapacidadAdicionalMaxRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:plan_capacidad_adicional_max_list')
        else:
            return render(request, 'dashboard/plan_capacidad_adicional_max_register.html', {'form': form})
    else:
        form = PlanCapacidadAdicionalMaxRegisterForm()
        return render(request, 'dashboard/plan_capacidad_adicional_max_register.html', {'form': form})


def plan_capacidad_adicional_max_edit(request, id):
    form = None
    error = None
    try:
        plan_capacidad_adicional_max = PlanCapacidadAdicionalMax.objects.get(id = id)
        if request.method == 'GET':
            form = PlanCapacidadAdicionalMaxRegisterForm(instance = plan_capacidad_adicional_max)
        else:
            form = PlanCapacidadAdicionalMaxRegisterForm(request.POST, instance = plan_capacidad_adicional_max)
            if form.is_valid():
                form.save()
                return redirect('dashboard:plan_capacidad_adicional_max_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/plan_capacidad_adicional_max_register.html', {'form': form, 'error': error})
