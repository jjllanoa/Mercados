from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.core.exceptions import ObjectDoesNotExist
# from dashboard.models import 
# from dashboard.forms.dashboard_form import 


@login_required(login_url='dashboard:login')
def index(request):
    return render(request, 'dashboard/index.html')


# def DemCaracList(request):
#     datos = DemCarac.objects.all()
#     return render(request, 'dashboard/demcarac_list.html', {'datos': datos})


# def DemCaracRegister(request):
#     if request.method == 'POST':
#         form = DemCaracRegisterForm(request.POST)
#         if form.is_valid():
#             # form.save()
#             return redirect('dashboard:demcarac_list')
#         else:
#             return render(request, 'dashboard/demcarac_register.html', {'form': form})
#     else:
#         form = DemCaracRegisterForm()
#         return render(request, 'dashboard/demcarac_register.html', {'form': form})


# def DemCaracEdit(request, id):
#     form = None
#     error = None
#     try:
#         demcarac = DemCarac.objects.get(id = id)
#         if request.method == 'GET':
#             form = DemCaracRegisterForm(instance = demcarac)
#         else:
#             form = DemCaracRegisterForm(request.POST, instance = demcarac)
#             if form.is_valid():
#                 # form.save()
#                 return redirect('dashboard:demcarac_list')

#     except ObjectDoesNotExist as e:
#         error = e

#     return render(request, 'dashboard/demcarac_register.html', {'form': form, 'error': error})


# def DemCaracDelete(request, id):
#     demcarac = DemCarac.objects.get(id = id)
#     if request.method == 'POST':
#         # demcarac.delete()
#         return redirect('dashboard:demcarac_list')

#     return render(request, 'dashboard/demcarac_delete.html', {'demcarac': demcarac})


# def MatrizActualList(request):
#     datos_matrizactualdc = MatrizActualDC.objects.all()
#     datos_matrizactualndc = MatrizActualNDC.objects.all()
#     return render(request, 'dashboard/matrizactual_list.html', {'datos_matrizactualdc': datos_matrizactualdc, 'datos_matrizactualndc': datos_matrizactualndc})


# def MatrizActualDCRegister(request):
#     if request.method == 'POST':
#         form = MatrizActualDCRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard:matrizactual_list')
#         else:
#             return render(request, 'dashboard/matrizactual_register.html', {'form': form})
#     else:
#         form = MatrizActualDCRegisterForm()
#         return render(request, 'dashboard/matrizactual_register.html', {'form': form})


# def MatrizActualNDCRegister(request):
#     if request.method == 'POST':
#         form = MatrizActualNDCRegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard:matrizactual_list')
#         else:
#             return render(request, 'dashboard/matrizactual_register.html', {'form': form})
#     else:
#         form = MatrizActualNDCRegisterForm()
#         return render(request, 'dashboard/matrizactual_register.html', {'form': form})


# def DemandaList(request):
#     datos = Demanda.objects.all()
#     return render(request, 'dashboard/demanda_list.html', {'datos': datos})


# def DemandaRegister(request):
#     if request.method == 'POST':
#         form = DemandaRegisterForm(request.POST)
#         if form.is_valid():
            
#             demanda_energia_dia = form.cleaned_data.get('demanda_energia') / form.cleaned_data.get('dia_mes')
#             form.save()
#             return redirect('dashboard:demanda_list')
#         else:
#             return render(request, 'dashboard/demanda_register.html', {'form': form})
#     else:
#         form = DemandaRegisterForm()
#         return render(request, 'dashboard/demanda_register.html', {'form': form})


# def DemandaEdit(request, id):
#     form = None
#     error = None
#     try:
#         demanda = Demanda.objects.get(id = id)
#         if request.method == 'GET':
#             form = DemandaRegisterForm(instance = demanda)
#         else:
#             form = DemandaRegisterForm(request.POST, instance = demanda)
#             if form.is_valid():
#                 demanda.demanda_energia_dia = demanda.demanda_energia / demanda.dia_mes
#                 form.save()
#                 return redirect('dashboard:demanda_list')

#     except ObjectDoesNotExist as e:
#         error = e

#     return render(request, 'dashboard/demanda_register.html', {'form': form, 'error': error})


# def PlantasList(request):
#     datos = Plantas.objects.all()
#     return render(request, 'dashboard/plantas_list.html', {'datos': datos})


# def PlantaRegister(request):
#     if request.method == 'POST':
#         form = PlantaRegisterForm(request.POST)
#         if form.is_valid():
#             # form.save()
#             return redirect('dashboard:plantas_list')
#         else:
#             return render(request, 'dashboard/planta_register.html', {'form': form})
#     else:
#         form = PlantaRegisterForm()
#         return render(request, 'dashboard/planta_register.html', {'form': form})


# def CxCList(request):
#     datos = CxC.objects.all()
#     return render(request, 'dashboard/cxc_list.html', {'datos': datos})


# def CLPList(request):
#     datos = CLP.objects.all()
#     return render(request, 'dashboard/clp_list.html', {'datos': datos})


# def ConsolidadoExistenteList(request):
#     datos = ConsolidadoExistente.objects.all()
#     return render(request, 'dashboard/consolidadoexistente_list.html', {'datos': datos})
