from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import Planta
from dashboard.forms.planta_form import PlantaRegisterForm
# from django.http import HttpResponse
import pandas as pd
import numpy as np
# import re


def planta_list(request):
    datos = Planta.objects.all()
    return render(request, 'dashboard/planta_list.html', {'datos': datos})


def planta_register(request):
    if request.method == 'POST':
        form = PlantaRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:planta_list')
        else:
            return render(request, 'dashboard/planta_register.html', {'form': form})
    else:
        form = PlantaRegisterForm()
        return render(request, 'dashboard/planta_register.html', {'form': form})


def planta_import(request):
    if request.method == 'POST':

        try:
            df = pd.read_excel(request.FILES['file'])

            # Nombres del archivo y los de la BD
            dict_nombres = {
                'col1':'agente',
                'col2':'planta',
                'col3':'tipo',
                'col4':'dc_ndc',
                'col5':'clasificacion',
                'col6':'contrato',
                'col7':'enficc_verificada',
                'col8':'enficc_no_comprometida',
                'col9':'fecha_inicio_vigencia_enficc',
                'col10':'fecha_fin_vigencia_enficc',
                'col11':'combustible_declarado'
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
            df['fecha_inicio_vigencia_enficc'] = pd.to_datetime(df['fecha_inicio_vigencia_enficc'], format="%Y/%m/%d")
            df['fecha_fin_vigencia_enficc'] = pd.to_datetime(df['fecha_fin_vigencia_enficc'], format="%Y/%m/%d")

            # Convertir toda los datos de la df a str para poder realizar la insercion en la bd
            df = df.astype(str)

            # Reemplazar los datos vacios o guiones en None's para realizar la insercion en la bd
            df.replace(to_replace=["nan", " - ", "NaT"], value=[None, None, None], inplace=True)

            # Borrar todos los datos de la tabla para realizar la nueva insercion
            Planta.objects.all().delete()

            for index, row in df.iterrows():
                instance = Planta(
                    agente=row[0],
                    planta=row[1],
                    tipo=row[2],
                    dc_ndc=row[3],
                    clasificacion=row[4],
                    contrato=row[5],
                    enficc_verificada=row[6],
                    enficc_no_comprometida=row[7],
                    fecha_inicio_vigencia_enficc=row[8],
                    fecha_fin_vigencia_enficc=row[9],
                    combustible_declarado=row[10]
                )
                instance.save()

        except Exception as e:
            print(e)

        return redirect('dashboard:planta_list')
    else:
        return render(request, 'dashboard/import_file.html')


def planta_edit(request, id):
    form = None
    error = None
    try:
        planta = Planta.objects.get(id = id)
        if request.method == 'GET':
            form = PlantaRegisterForm(instance = planta)
        else:
            form = PlantaRegisterForm(request.POST, instance = planta)
            if form.is_valid():
                form.save()
                return redirect('dashboard:planta_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/planta_register.html', {'form': form, 'error': error})
