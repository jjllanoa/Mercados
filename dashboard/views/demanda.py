from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import Demanda
from dashboard.forms.demanda_form import DemandaRegisterForm
import pandas as pd
import numpy as np


def demanda_list(request):
    datos = Demanda.objects.all()
    return render(request, 'dashboard/demanda_list.html', {'datos': datos})


def demanda_register(request):
    if request.method == 'POST':
        form = DemandaRegisterForm(request.POST)
        if form.is_valid():
            # demcarac = DemCarac.objects
            # form.demanda_energia_dia = form.cleaned_data.get('demanda_energia') / form.cleaned_data.get('dia_mes')
            instance = form.save()
            instance.demanda_energia_dia = 123
            instance.save()
            return redirect('dashboard:demanda_list')
        else:
            return render(request, 'dashboard/demanda_register.html', {'form': form})
    else:
        form = DemandaRegisterForm()
        return render(request, 'dashboard/demanda_register.html', {'form': form})


def demanda_import(request):
    if request.method == 'POST':

        try:
            df = pd.read_excel(request.FILES['file'])

            # Nombres del archivo y los de la BD
            dict_nombres = {
                'col1':'fecha',
                'col2':'demanda_energia'
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

            df['dia_mes'] = df['fecha'].dt.daysinmonth
            df['demanda_energia'] = df['demanda_energia'].astype(float)
            df['demanda_energia_dia'] = df['demanda_energia'] / df['dia_mes']

            # Convertir toda los datos de la df a str para poder realizar la insercion en la bd
            df = df.astype(str)

            # Reemplazar los datos vacios o guiones en None's para realizar la insercion en la bd
            df.replace(to_replace=["nan", " - ", "NaT"], value=[None, None, None], inplace=True)

            # Borrar todos los datos de la tabla para realizar la nueva insercion
            Demanda.objects.all().delete()

            for index, row in df.iterrows():
                # instance = Demanda(
                #     fecha=row[0],
                #     demanda_energia=row[1],
                #     dia_mes=row[2],
                #     demanda_energia_dia=row[3]
                # )
                # instance.save()
                print(row[0])
                print(row[1])
                print(row[2])
                print(row[3])
                print('-------')

        except Exception as e:
            print(e)

        return redirect('dashboard:demanda_list')
    else:
        return render(request, 'dashboard/import_file.html')


def demanda_edit(request, id):
    form = None
    error = None
    try:
        demanda = Demanda.objects.get(id = id)
        if request.method == 'GET':
            form = DemandaRegisterForm(instance = demanda)
        else:
            form = DemandaRegisterForm(request.POST, instance = demanda)
            if form.is_valid():
                demanda.demanda_energia_dia = demanda.demanda_energia / demanda.dia_mes
                # datos_query = DemCarac.objects.get(id = 1)
                # print(datos_query)#.update(total_d=F('total_d') + F('total_h'))
                form.save()
                return redirect('dashboard:demanda_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/demanda_register.html', {'form': form, 'error': error})
