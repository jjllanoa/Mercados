from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import DemCarac
from dashboard.forms.demcarac_form import DemCaracRegisterForm
from django.http import HttpResponse
import pandas as pd
import numpy as np


def demcarac_list(request):
    datos = DemCarac.objects.all()
    return render(request, 'dashboard/demcarac_list.html', {'datos': datos})


def demcarac_register(request):
    if request.method == 'POST':
        form = DemCaracRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:demcarac_list')
        else:
            return render(request, 'dashboard/demcarac_register.html', {'form': form})
    else:
        form = DemCaracRegisterForm()
        return render(request, 'dashboard/demcarac_register.html', {'form': form})


def demcarac_import(request):
    if request.method == 'POST':

        try:

            df = pd.read_excel(request.FILES['file'])

            # Nombres del archivo y los de la BD
            dict_nombres = {
                'col1':'bloque',
                'col2':'duracion',
                'col3':'restup',
                'col4':'restdn',
            }

            # Validar los nombres del archivo con los de la BD
            for nom_col in dict_nombres.keys():
                if nom_col not in df.columns:
                    raise NameError(f'La columna {nom_col} no se encuentra en el archivo')

            # Reemplazar los nombres
            df.rename(columns=dict_nombres, inplace=True)

            # Tomar las columnas deseadasde la df
            df = df[dict_nombres.values()]

            print(df)
            # df = re.sub("' - '", 'NULL', df)
            df = df.replace(" - ", "0")
            # datos = re.sub("'None'", 'NULL', str(datos)[1:-1])
            # datos = re.sub('"', '', datos)
            # datos = re.sub("'nan'", 'NULL', datos)
            # datos = re.sub("' - '", 'NULL', datos)
            # datos = re.sub("'NaT'", 'NULL', datos)
            print(df)

            # Antes de pasar toda la df a string, se debe convertir por separado la columna numerica a string considerando
            # el formato que queremos darle, el no realizar esto generara resultados muy diferentes y del que aparentemente
            # no se sabe de donde se originan las diferencias
            for col in df.columns:
                if df[col].dtype == np.float64:
                    df[col] = df[col].apply(lambda x: '{0:.30f}'.format(x))

            # Convertir toda los datos de la df a str para poder realizar la insercion en la bd
            df = df.astype(str)

            # print(df)
            DemCarac.objects.all().delete()
            for index, row in df.iterrows():

                instance = DemCarac(bloque=row[0], duracion=row[1], restup=row[2], restdn=row[3])
                instance.save()
                print(row[0])
                print(row[1])
                print(row[2])
                print(row[3])
                print('-------')

        # print(request.FILES['file'])
        # return HttpResponse("return this string")
        except Exception as e:
            print(e)

        return redirect('dashboard:demcarac_list')
            # form.save()
            # return redirect('dashboard:clp_list')
        # else:
        #     return render(request, 'dashboard/prueba.html', {'form': form})
    else:
        # form = PruebaRegisterForm()
        return render(request, 'dashboard/import_file.html')


def demcarac_edit(request, id):
    form = None
    error = None
    try:
        demcarac = DemCarac.objects.get(id = id)
        if request.method == 'GET':
            form = DemCaracRegisterForm(instance = demcarac)
        else:
            form = DemCaracRegisterForm(request.POST, instance = demcarac)
            if form.is_valid():
                print('text')
                instance = form.save()
                instance.duracion = 5.0
                # demanda = Demanda.objects.get(id = )
                instance.save()
                return redirect('dashboard:demcarac_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/demcarac_register.html', {'form': form, 'error': error})


def demcarac_delete(request, id):
    datos = DemCarac.objects.get(id = id)
    if request.method == 'POST':
        # demcarac.delete()
        return redirect('dashboard:demcarac_list')

    return render(request, 'dashboard/demcarac_delete.html', {'datos': datos})
