from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import MetaMatriz, RegresionMetaMatriz
# from dashboard.forms.meta_matriz_form import MetaMatrizRegisterForm
import pandas as pd


def meta_matriz_list(request):
    datos = MetaMatriz.objects.all()
    return render(request, 'dashboard/meta_matriz_list.html', {'datos': datos})


def meta_matriz_register(request):
    if request.method == 'POST':

        # RegresionMetaMatriz.objects.all()
        df = pd.DataFrame()
        df['eolica'] = [dato.eolica for dato in RegresionMetaMatriz.objects.all()]
        df['solar'] = [dato.solar for dato in RegresionMetaMatriz.objects.all()]
        df['pch'] = [dato.pch for dato in RegresionMetaMatriz.objects.all()]
        df['ndc_t'] = [dato.ndc_t for dato in RegresionMetaMatriz.objects.all()]
        df['ernc'] = [dato.ernc for dato in RegresionMetaMatriz.objects.all()]
        df['liquidos'] = [dato.liquidos for dato in RegresionMetaMatriz.objects.all()]
        df['carbon'] = [dato.carbon for dato in RegresionMetaMatriz.objects.all()]
        df['gas'] = [dato.gas for dato in RegresionMetaMatriz.objects.all()]
        df['glp'] = [dato.glp for dato in RegresionMetaMatriz.objects.all()]
        df['termica'] = [dato.termica for dato in RegresionMetaMatriz.objects.all()]
        df['hidraulica'] = [dato.hidraulica for dato in RegresionMetaMatriz.objects.all()]
        df = df/100
        df = df.round(4)
        df['fecha'] = [dato.fecha for dato in RegresionMetaMatriz.objects.all()]
        print(df)

        # year = np.array([dato.fecha for dato in PlanMetaMatriz.objects.all()])
        # years = np.arange(year[0], year[-1]+1)
        # items = dict()
        # items['liquidos'] = [dato.liquidos for dato in PlanMetaMatriz.objects.all()]
        # items['carbon'] = [dato.carbon for dato in PlanMetaMatriz.objects.all()]
        # items['gas'] = [dato.gas for dato in PlanMetaMatriz.objects.all()]
        # items['glp'] = [dato.glp for dato in PlanMetaMatriz.objects.all()]

        # df_items = pd.DataFrame(items)
        # df = pd.DataFrame(years, columns=['fecha'])

        # for col in df_items.columns:
        #     degree=3
        #     polyreg=make_pipeline(PolynomialFeatures(degree),LinearRegression())
        #     polyreg.fit(year.reshape(-1,1), df_items[col].values)
        #     minimo = np.min(df_items[col])
        #     column = polyreg.predict(years.reshape(-1,1))
        #     column[column<minimo] = minimo
        #     df[col] = column

        # df['termica'] = df['liquidos']+df['carbon']+df['gas']+df['glp']
        # df = df.round(1)
        # print(df)

        # DemCarac.objects.all().delete()
        # for index, row in df.iterrows():

        #     instance = DemCarac(bloque=row[0], duracion=row[1], restup=row[2], restdn=row[3])
        #     instance.save()
        #     print(row[0])
        #     print(row[1])
        #     print(row[2])
        #     print(row[3])
        #     print('-------')

        # datos = PlanMetaMatriz.objects.all()
        # datos = PlanMetaMatriz.objects.filter(fecha=year[0]).first()

        # print(type(datos))
        # form = DemCaracRegisterForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('dashboard:demcarac_list')
        # else:
        # return HttpResponse("return this string")
        return redirect('dashboard:meta_matriz_list')
    else:
        # form = DemCaracRegisterForm()
        return render(request, 'dashboard/prueba.html',)


def meta_matriz_edit(request, id):
    form = None
    error = None
    try:
        meta_matriz = MetaMatriz.objects.get(id = id)
        if request.method == 'GET':
            form = MetaMatrizRegisterForm(instance = meta_matriz)
        else:
            form = MetaMatrizRegisterForm(request.POST, instance = meta_matriz)
            if form.is_valid():
                form.save()
                return redirect('dashboard:meta_matriz_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/meta_matriz_register.html', {'form': form, 'error': error})
