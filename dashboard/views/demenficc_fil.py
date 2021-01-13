from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import DemENFICCFil, PlanEnergiaFirmeDemanda, Demanda, ExistenteCxCCLP
from dashboard.forms.demenficc_fil_form import DemENFICCFilRegisterForm
from django.http import HttpResponse
import numpy as np


def demenficc_fil_list(request):
    datos = DemENFICCFil.objects.all()
    return render(request, 'dashboard/demenficc_fil_list.html', {'datos': datos})


def demenficc_fil_register(request):
    if request.method == 'POST':
        # instance = DemCarac(bloque=row[0], duracion=row[1], restup=row[2], restdn=row[3])
        #     instance.save()

        year_inicial = [dato.fecha_inicial for dato in PlanEnergiaFirmeDemanda.objects.all()]
        year_final = [dato.fecha_final for dato in PlanEnergiaFirmeDemanda.objects.all()]
        years = np.arange(year_inicial[0], year_final[0]+1)

        # DemENFICCFil.objects.all().delete()

        for year in years:
            # print(year)
            for month in range(1, 13):
                # print(month)
                demanda = Demanda.objects.filter(fecha__year = year, fecha__month = month, fecha__day = 1).first()
                existentecxcclp = ExistenteCxCCLP.objects.filter(fecha__year = year, fecha__month = month, fecha__day = 1).first()

                if (demanda is not None) and (existentecxcclp is not None):
                    # instance = DemENFICCFil(
                    #     fecha=demanda.fecha,
                    #     demanda_energia=demanda.demanda_energia,
                    #     enficc=existentecxcclp.existente_cxc_clp * demanda.dia_mes
                    # )
                    # instance.save()
                    print(demanda.fecha)
                    print(demanda.demanda_energia)
                    print(demanda.dia_mes)
                    print(existentecxcclp.existente_cxc_clp)
                    print('-----------------------')
                    print(existentecxcclp.existente_cxc_clp * demanda.dia_mes)
                    print('----------Fin----------')






        # form = DemENFICCFilRegisterForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('dashboard:demenficc_fil_list')
        # else:
        #     return render(request, 'dashboard/demenficc_fil_register.html', {'form': form})
        return redirect('dashboard:demenficc_fil_list')
        # return HttpResponse("Datos generados con exito")
    else:
        # form = DemENFICCFilRegisterForm()
        return render(request, 'dashboard/prueba.html')


def demenficc_fil_edit(request, id):
    form = None
    error = None
    try:
        demenficc_fil = DemENFICCFil.objects.get(id = id)
        if request.method == 'GET':
            form = DemENFICCFilRegisterForm(instance = demenficc_fil)
        else:
            form = DemENFICCFilRegisterForm(request.POST, instance = demenficc_fil)
            if form.is_valid():
                form.save()
                return redirect('dashboard:demenficc_fil_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/demenficc_fil_register.html', {'form': form, 'error': error})
