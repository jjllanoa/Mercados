from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import CLP
from dashboard.forms.form_prueba import PruebaRegisterForm
from django.http import HttpResponse
import pandas as pd


def clp_list(request):
    datos = CLP.objects.all()
    return render(request, 'dashboard/clp_list.html', {'datos': datos})


def clp_register(request):
    if request.method == 'POST':
        # form = PruebaRegisterForm(request.POST)
        # if form.is_valid():

        # print(form.file)
        df = pd.read_excel(request.FILES['file'])
        print(df)
        for row in df.iterrows():
            print(row[0])
            print('-------')
            
        # print(request.FILES['file'])
        return HttpResponse("return this string")
            # form.save()
            # return redirect('dashboard:clp_list')
        # else:
        #     return render(request, 'dashboard/prueba.html', {'form': form})
    else:
        # form = PruebaRegisterForm()
        return render(request, 'dashboard/prueba.html')


# def clp_edit(request, id):
#     form = None
#     error = None
#     try:
#         clp = CLP.objects.get(id = id)
#         if request.method == 'GET':
#             form = CLPRegisterForm(instance = clp)
#         else:
#             form = CLPRegisterForm(request.POST, instance = clp)
#             if form.is_valid():

#                 if clp.tecnologia == "termica":
#                     clp.oef_asignada = float(clp.capacidad)*24*0.9/1000*1000000

#                 if clp.tecnologia == "solar":
#                     clp.oef_asignada = float(clp.capacidad)*24*0.144/1000*1000000

#                 if clp.tecnologia == "eolica":
#                     clp.oef_asignada = float(clp.capacidad)*24*0.18/1000*1000000

#                 if clp.tecnologia == "hidraulica":
#                     clp.oef_asignada = float(clp.capacidad)*24*0.4/1000*1000000

#                 form.save()
#                 return redirect('dashboard:clp_list')

#     except ObjectDoesNotExist as e:
#         error = e

#     return render(request, 'dashboard/clp_register.html', {'form': form, 'error': error})
