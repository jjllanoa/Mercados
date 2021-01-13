from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import PlanMetaMatriz, PlanMetaMatrizERNC, RegresionMetaMatriz
# from dashboard.forms.demcarac_form import DemCaracRegisterForm
# from django.http import HttpResponse
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np


# def demcarac_list(request):
#     datos = DemCarac.objects.all()
#     return render(request, 'dashboard/demcarac_list.html', {'datos': datos})


def regresiones_register(request):
    if request.method == 'POST':
        # years = list()
        # for dato in PlanMetaMatriz.objects.all():
        #    years.append(dato.fecha)
        #    print(dato.fecha)

        year = np.array([dato.fecha for dato in PlanMetaMatriz.objects.all()])
        years = np.arange(year[0], year[-1]+1)
        items = dict()
        items['liquidos'] = [dato.liquidos for dato in PlanMetaMatriz.objects.all()]
        items['carbon'] = [dato.carbon for dato in PlanMetaMatriz.objects.all()]
        items['gas'] = [dato.gas for dato in PlanMetaMatriz.objects.all()]
        items['glp'] = [dato.glp for dato in PlanMetaMatriz.objects.all()]

        df_items = pd.DataFrame(items)
        df1 = pd.DataFrame(years, columns=['fecha'])

        for col in df_items.columns:
            degree=3
            polyreg=make_pipeline(PolynomialFeatures(degree),LinearRegression())
            polyreg.fit(year.reshape(-1,1), df_items[col].values)
            minimo = np.min(df_items[col])
            column = polyreg.predict(years.reshape(-1,1))
            column[column<minimo] = minimo
            df1[col] = column

        df1['termica'] = df1['liquidos'] + df1['carbon'] + df1['gas'] + df1['glp']

        year = np.array([dato.fecha for dato in PlanMetaMatrizERNC.objects.all()])
        years = np.arange(year[0], year[-1]+1)
        items = dict()
        items['eolica'] = [dato.eolica for dato in PlanMetaMatrizERNC.objects.all()]
        items['solar'] = [dato.solar for dato in PlanMetaMatrizERNC.objects.all()]
        items['pch'] = [dato.pch for dato in PlanMetaMatrizERNC.objects.all()]
        items['ndc_t'] = [dato.ndc_t for dato in PlanMetaMatrizERNC.objects.all()]

        df_items = pd.DataFrame(items)
        df2 = pd.DataFrame(years, columns=['fecha'])

        for col in df_items.columns:
            degree=3
            polyreg=make_pipeline(PolynomialFeatures(degree),LinearRegression())
            polyreg.fit(year.reshape(-1,1), df_items[col].values)
            minimo = np.min(df_items[col])
            column = polyreg.predict(years.reshape(-1,1))
            column[column<minimo] = minimo
            df2[col] = column

        df2['ernc'] = df2['eolica'] + df2['solar'] + df2['pch'] + df2['ndc_t']

        df1['hidraulica'] = 100 - (df1['termica'] + df2['ernc'])

        df = pd.merge(df1, df2)
        df = df.round(4)

        print(df)

        # Borrar todos los datos de la tabla para realizar la nueva insercion
        # RegresionMetaMatriz.objects.all().delete()

        for index, row in df.iterrows():
            # instance = RegresionMetaMatriz(
            #     fecha=row[0],
            #     liquidos=row[1],
            #     carbon=row[2],
            #     gas=row[3],
            #     glp=row[4],
            #     termica=row[5],
            #     hidraulica=row[6],
            #     eolica=row[7],
            #     solar=row[8],
            #     pch=row[9],
            #     ndc_t=row[10],
            #     ernc=row[11]
            # )
            # instance.save()
            print(row[0])
            print(row[1])
            print(row[2])
            print(row[3])
            print(row[4])
            print(row[5])
            print(row[6])
            print(row[7])
            print(row[8])
            print(row[9])
            print(row[10])
            print(row[11])
            print('-------')

        # datos = PlanMetaMatriz.objects.all()
        # datos = PlanMetaMatriz.objects.filter(fecha=year[0]).first()

        # print(type(datos))
        # form = DemCaracRegisterForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('dashboard:demcarac_list')
        # else:
        # return HttpResponse("return this string")
        return redirect('dashboard:regresiones_register')
    else:
        # form = DemCaracRegisterForm()
        return render(request, 'dashboard/prueba.html',)


# def demcarac_import(request):
#     if request.method == 'POST':

#         try:

#             df = pd.read_excel(request.FILES['file'])

#             # Nombres del archivo y los de la BD
#             dict_nombres = {
#                 'col1':'bloque',
#                 'col2':'duracion',
#                 'col3':'restup',
#                 'col4':'restdn',
#             }

#             # Validar los nombres del archivo con los de la BD
#             for nom_col in dict_nombres.keys():
#                 if nom_col not in df.columns:
#                     raise NameError(f'La columna {nom_col} no se encuentra en el archivo')

#             # Reemplazar los nombres
#             df.rename(columns=dict_nombres, inplace=True)

#             # Tomar las columnas deseadasde la df
#             df = df[dict_nombres.values()]

#             print(df)
#             # df = re.sub("' - '", 'NULL', df)
#             df = df.replace(" - ", "0")
#             # datos = re.sub("'None'", 'NULL', str(datos)[1:-1])
#             # datos = re.sub('"', '', datos)
#             # datos = re.sub("'nan'", 'NULL', datos)
#             # datos = re.sub("' - '", 'NULL', datos)
#             # datos = re.sub("'NaT'", 'NULL', datos)
#             print(df)

#             # Antes de pasar toda la df a string, se debe convertir por separado la columna numerica a string considerando
#             # el formato que queremos darle, el no realizar esto generara resultados muy diferentes y del que aparentemente
#             # no se sabe de donde se originan las diferencias
#             for col in df.columns:
#                 if df[col].dtype == np.float64:
#                     df[col] = df[col].apply(lambda x: '{0:.30f}'.format(x))

#             # Convertir toda los datos de la df a str para poder realizar la insercion en la bd
#             df = df.astype(str)

#             # print(df)
#             DemCarac.objects.all().delete()
#             for index, row in df.iterrows():

#                 instance = DemCarac(bloque=row[0], duracion=row[1], restup=row[2], restdn=row[3])
#                 instance.save()
#                 print(row[0])
#                 print(row[1])
#                 print(row[2])
#                 print(row[3])
#                 print('-------')

#         # print(request.FILES['file'])
#         # return HttpResponse("return this string")
#         except Exception as e:
#             print(e)

#         return redirect('dashboard:demcarac_list')
#             # form.save()
#             # return redirect('dashboard:clp_list')
#         # else:
#         #     return render(request, 'dashboard/prueba.html', {'form': form})
#     else:
#         # form = PruebaRegisterForm()
#         return render(request, 'dashboard/import_file.html')


# def demcarac_edit(request, id):
#     form = None
#     error = None
#     try:
#         demcarac = DemCarac.objects.get(id = id)
#         if request.method == 'GET':
#             form = DemCaracRegisterForm(instance = demcarac)
#         else:
#             form = DemCaracRegisterForm(request.POST, instance = demcarac)
#             if form.is_valid():
#                 print('text')
#                 instance = form.save()
#                 instance.duracion = 5.0
#                 # demanda = Demanda.objects.get(id = )
#                 instance.save()
#                 return redirect('dashboard:demcarac_list')

#     except ObjectDoesNotExist as e:
#         error = e

#     return render(request, 'dashboard/demcarac_register.html', {'form': form, 'error': error})
