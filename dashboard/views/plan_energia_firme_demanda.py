from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import PlanEnergiaFirmeDemanda
from dashboard.forms.plan_energia_firme_demanda_form import PlanEnergiaFirmeDemandaRegisterForm


def plan_energia_firme_demanda_list(request):
    datos = PlanEnergiaFirmeDemanda.objects.all()
    return render(request, 'dashboard/plan_energia_firme_demanda_list.html', {'datos': datos})


def plan_energia_firme_demanda_edit(request, id):
    form = None
    error = None
    try:
        plan_energia_firme_demanda = PlanEnergiaFirmeDemanda.objects.get(id = id)
        if request.method == 'GET':
            form = PlanEnergiaFirmeDemandaRegisterForm(instance = plan_energia_firme_demanda)
        else:
            form = PlanEnergiaFirmeDemandaRegisterForm(request.POST, instance = plan_energia_firme_demanda)
            if form.is_valid():
                form.save()
                return redirect('dashboard:plan_energia_firme_demanda_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/plan_energia_firme_demanda_register.html', {'form': form, 'error': error})
