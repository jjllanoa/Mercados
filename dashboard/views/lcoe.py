from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import LCOE
from dashboard.forms.lcoe_form import LCOERegisterForm


def lcoe_list(request):
    datos = LCOE.objects.all()
    return render(request, 'dashboard/lcoe_list.html', {'datos': datos})


def lcoe_register(request):
    if request.method == 'POST':
        form = LCOERegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:lcoe_list')
        else:
            return render(request, 'dashboard/lcoe_register.html', {'form': form})
    else:
        form = LCOERegisterForm()
        return render(request, 'dashboard/lcoe_register.html', {'form': form})


def lcoe_edit(request, id):
    form = None
    error = None
    try:
        lcoe = LCOE.objects.get(id = id)
        if request.method == 'GET':
            form = LCOERegisterForm(instance = lcoe)
        else:
            form = LCOERegisterForm(request.POST, instance = lcoe)
            if form.is_valid():
                form.save()
                return redirect('dashboard:lcoe_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/lcoe_register.html', {'form': form, 'error': error})
