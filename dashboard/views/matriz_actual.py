from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import MatrizActualDC, MatrizActualNDC
from dashboard.forms.dashboard_form import MatrizActualDCRegisterForm, MatrizActualNDCRegisterForm
import pandas as pd
import numpy as np
# import re


def matriz_actual_list(request):
    datos_matriz_actual_dc = MatrizActualDC.objects.all()
    datos_matriz_actual_ndc = MatrizActualNDC.objects.all()
    return render(request, 'dashboard/matriz_actual_list.html', {'datos_matriz_actual_dc': datos_matriz_actual_dc, 'datos_matriz_actual_ndc': datos_matriz_actual_ndc})


def matriz_actual_dc_register(request):
    if request.method == 'POST':
        form = MatrizActualDCRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:matriz_actual_list')
        else:
            return render(request, 'dashboard/matriz_actual_register.html', {'form': form})
    else:
        form = MatrizActualDCRegisterForm()
        return render(request, 'dashboard/matriz_actual_register.html', {'form': form})


def matriz_actual_dc_import(request):
    if request.method == 'POST':

        try:
            df = pd.read_excel(request.FILES['file'])

            # Nombres del archivo y los de la BD
            dict_nombres = {
                'col1':'tipo',
                'col2':'capacidad',
                'col3':'conversion',
                'col4':'fecha'
            }

            # Validar los nombres del archivo con los de la BD
            for nom_col in dict_nombres.keys():
                if nom_col not in df.columns:
                    raise NameError(f'La columna {nom_col} no se encuentra en el archivo')

            # Reemplazar los nombres
            df.rename(columns=dict_nombres, inplace=True)

            # Tomar las columnas deseadasde la df
            df = df[dict_nombres.values()]

            # Antes de pasar toda la df a string, se debe convertir por separado la columna numerica a string considerando
            # el formato que queremos darle, el no realizar esto generara resultados muy diferentes y del que aparentemente
            # no se sabe de donde se originan las diferencias
            for col in df.columns:
                if df[col].dtype == np.float64:
                    df[col] = df[col].apply(lambda x: '{0:.30f}'.format(x))

            # Organizar las fechas con el formato deseado
            df['fecha'] = pd.to_datetime(df['fecha'], format="%Y/%m/%d")

            # Convertir toda los datos de la df a str para poder realizar la insercion en la bd
            df = df.astype(str)

            # Reemplazar los datos vacios o guiones en None's para realizar la insercion en la bd
            df.replace(to_replace=["nan", " - ", "NaT"], value=[None, None, None], inplace=True)

            # Borrar todos los datos de la tabla para realizar la nueva insercion
            MatrizActualDC.objects.all().delete()

            for index, row in df.iterrows():
                instance = MatrizActualDC(
                    tipo=row[0],
                    capacidad=row[1],
                    conversion=row[2],
                    fecha=row[3]
                )
                instance.save()

        except Exception as e:
            print(e)

        return redirect('dashboard:matriz_actual_list')
    else:
        return render(request, 'dashboard/import_file.html')


def matriz_actual_ndc_register(request):
    if request.method == 'POST':
        form = MatrizActualNDCRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:matriz_actual_list')
        else:
            return render(request, 'dashboard/matriz_actual_register.html', {'form': form})
    else:
        form = MatrizActualNDCRegisterForm()
        return render(request, 'dashboard/matriz_actual_register.html', {'form': form})
