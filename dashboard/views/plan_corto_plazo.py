from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import PlanCortoPlazo
from dashboard.forms.plan_corto_plazo_form import PlanCortoPlazoRegisterForm


def plan_corto_plazo_list(request):
    datos = PlanCortoPlazo.objects.all()
    return render(request, 'dashboard/plan_corto_plazo_list.html', {'datos': datos})


def plan_corto_plazo_register(request):
    if request.method == 'POST':
        form = PlanCortoPlazoRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:corto_plazo_list')
        else:
            return render(request, 'dashboard/plan_corto_plazo_register.html', {'form': form})
    else:
        form = PlanCortoPlazoRegisterForm()
        return render(request, 'dashboard/plan_corto_plazo_register.html', {'form': form})


def plan_corto_plazo_edit(request, id):
    form = None
    error = None
    try:
        plan_corto_plazo = PlanCortoPlazo.objects.get(id = id)
        if request.method == 'GET':
            form = PlanCortoPlazoRegisterForm(instance = plan_corto_plazo)
        else:
            form = PlanCortoPlazoRegisterForm(request.POST, instance = plan_corto_plazo)
            if form.is_valid():
                form.save()
                return redirect('dashboard:plan_corto_plazo_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/plan_corto_plazo_register.html', {'form': form, 'error': error})
