from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import PlanMetaMatrizERNC, CrecimientoMW
from dashboard.forms.plan_meta_matriz_ernc_form import PlanMetaMatrizERNCRegisterForm


def plan_meta_matriz_ernc_list(request):
    datos = PlanMetaMatrizERNC.objects.all()
    # crecimiento = CrecimientoMW.objects.filter(fecha__year = 2023, fecha__month = 12, fecha__day = 1).first()
    # print(crecimiento)
    # eolica = 0
    # if crecimiento is not None:

    #     eolica = (crecimiento.eolica / crecimiento.total)*100
        
    #     print(eolica)
    return render(request, 'dashboard/plan_meta_matriz_ernc_list.html', {'datos': datos})


def plan_meta_matriz_ernc_register(request):
    if request.method == 'POST':
        form = PlanMetaMatrizERNCRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:plan_meta_matriz_ernc_list')
        else:
            return render(request, 'dashboard/plan_meta_matriz_ernc_register.html', {'form': form})
    else:
        form = PlanMetaMatrizERNCRegisterForm()
        return render(request, 'dashboard/plan_meta_matriz_ernc_register.html', {'form': form})


def plan_meta_matriz_ernc_edit(request, id):
    form = None
    error = None
    try:
        plan_meta_matriz_ernc = PlanMetaMatrizERNC.objects.get(id = id)
        if request.method == 'GET':
            form = PlanMetaMatrizERNCRegisterForm(instance = plan_meta_matriz_ernc)
        else:
            form = PlanMetaMatrizERNCRegisterForm(request.POST, instance = plan_meta_matriz_ernc)

            if form.is_valid():
                crecimiento_mw = CrecimientoMW.objects.filter(fecha__year = plan_meta_matriz_ernc.fecha, fecha__month = 12, fecha__day = 1).first()

                if (plan_meta_matriz_ernc.eolica == 0) or (plan_meta_matriz_ernc.eolica == None):
                    plan_meta_matriz_ernc.eolica = 0
                    if crecimiento_mw is not None:
                        plan_meta_matriz_ernc.eolica = (crecimiento_mw.eolica / crecimiento_mw.total)*100

                if (plan_meta_matriz_ernc.solar == 0) or (plan_meta_matriz_ernc.solar == None):
                    plan_meta_matriz_ernc.solar = 0
                    if crecimiento_mw is not None:
                        plan_meta_matriz_ernc.solar = (crecimiento_mw.solar / crecimiento_mw.total)*100

                if (plan_meta_matriz_ernc.pch == 0) or (plan_meta_matriz_ernc.pch == None):
                    plan_meta_matriz_ernc.pch = 0
                    if crecimiento_mw is not None:
                        plan_meta_matriz_ernc.pch = (crecimiento_mw.pch / crecimiento_mw.total)*100

                if (plan_meta_matriz_ernc.ndc_t == 0) or (plan_meta_matriz_ernc.ndc_t == None):
                    plan_meta_matriz_ernc.ndc_t = 0
                    if crecimiento_mw is not None:
                        plan_meta_matriz_ernc.ndc_t = (crecimiento_mw.ndc_t / crecimiento_mw.total)*100

                # if crecimiento_mw is not None:
                #     meta_matriz_ernc.eolica = (crecimiento_mw.eolica / crecimiento_mw.total)*100
                #     meta_matriz_ernc.solar = (crecimiento_mw.solar / crecimiento_mw.total)*100
                #     meta_matriz_ernc.pch = (crecimiento_mw.pch / crecimiento_mw.total)*100
                #     meta_matriz_ernc.ndc_t = (crecimiento_mw.ndc_t / crecimiento_mw.total)*100

                plan_meta_matriz_ernc.ernc = plan_meta_matriz_ernc.eolica + plan_meta_matriz_ernc.solar + plan_meta_matriz_ernc.pch + plan_meta_matriz_ernc.ndc_t

                form.save()
                return redirect('dashboard:plan_meta_matriz_ernc_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/plan_meta_matriz_ernc_register.html', {'form': form, 'error': error})
