from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import PlanMetaMatriz, CrecimientoMW
from dashboard.forms.plan_meta_matriz_form import PlanMetaMatrizRegisterForm


def plan_meta_matriz_list(request):
    datos = PlanMetaMatriz.objects.all()
    return render(request, 'dashboard/plan_meta_matriz_list.html', {'datos': datos})


def plan_meta_matriz_register(request):
    if request.method == 'POST':
        form = PlanMetaMatrizRegisterForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('dashboard:plan_meta_matriz_list')
        else:
            return render(request, 'dashboard/plan_meta_matriz_register.html', {'form': form})
    else:
        form = PlanMetaMatrizRegisterForm()
        return render(request, 'dashboard/plan_meta_matriz_register.html', {'form': form})


def plan_meta_matriz_edit(request, id):
    form = None
    error = None
    try:
        plan_meta_matriz = PlanMetaMatriz.objects.get(id = id)
        if request.method == 'GET':
            form = PlanMetaMatrizRegisterForm(instance = plan_meta_matriz)
        else:
            form = PlanMetaMatrizRegisterForm(request.POST, instance = plan_meta_matriz)

            if form.is_valid():
                crecimiento_mw = CrecimientoMW.objects.filter(fecha__year = plan_meta_matriz.fecha, fecha__month = 12, fecha__day = 1).first()

                if (plan_meta_matriz.liquidos == 0) or (plan_meta_matriz.liquidos == None):
                    plan_meta_matriz.liquidos = 0
                    if crecimiento_mw is not None:
                        plan_meta_matriz.liquidos = (crecimiento_mw.liquidos / crecimiento_mw.total)*100

                if (plan_meta_matriz.carbon == 0) or (plan_meta_matriz.carbon == None):
                    plan_meta_matriz.carbon = 0
                    if crecimiento_mw is not None:
                        plan_meta_matriz.carbon = (crecimiento_mw.carbon / crecimiento_mw.total)*100

                if (plan_meta_matriz.gas == 0) or (plan_meta_matriz.gas == None):
                    plan_meta_matriz.gas = 0
                    if crecimiento_mw is not None:
                        plan_meta_matriz.gas = (crecimiento_mw.gas / crecimiento_mw.total)*100

                if (plan_meta_matriz.glp == 0) or (plan_meta_matriz.glp == None):
                    plan_meta_matriz.glp = 0
                    if crecimiento_mw is not None:
                        plan_meta_matriz.glp = (crecimiento_mw.glp / crecimiento_mw.total)*100

                if (plan_meta_matriz.hidraulica == 0) or (plan_meta_matriz.hidraulica == None):
                    plan_meta_matriz.hidraulica = 0
                    if crecimiento_mw is not None:
                        plan_meta_matriz.hidraulica = (crecimiento_mw.hidraulica / crecimiento_mw.total)*100

                form.save()
                return redirect('dashboard:plan_meta_matriz_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/plan_meta_matriz_register.html', {'form': form, 'error': error})
