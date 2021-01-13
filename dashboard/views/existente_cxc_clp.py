from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import ExistenteCxCCLP
from dashboard.forms.existente_cxc_clp_form import ExistenteCxCCLPRegisterForm


def existente_cxc_clp_list(request):
    datos = ExistenteCxCCLP.objects.all()
    return render(request, 'dashboard/existente_cxc_clp_list.html', {'datos': datos})


def existente_cxc_clp_register(request):
    if request.method == 'POST':
        form = ExistenteCxCCLPRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:existente_cxc_clp_list')
        else:
            return render(request, 'dashboard/existente_cxc_clp_register.html', {'form': form})
    else:
        form = ExistenteCxCCLPRegisterForm()
        return render(request, 'dashboard/existente_cxc_clp_register.html', {'form': form})


def existente_cxc_clp_edit(request, id):
    form = None
    error = None
    try:
        existente_cxc_clp = ExistenteCxCCLP.objects.get(id = id)
        if request.method == 'GET':
            form = ExistenteCxCCLPRegisterForm(instance = existente_cxc_clp)
        else:
            form = ExistenteCxCCLPRegisterForm(request.POST, instance = existente_cxc_clp)
            if form.is_valid():
                form.save()
                return redirect('dashboard:existente_cxc_clp_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/existente_cxc_clp_register.html', {'form': form, 'error': error})
