from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from dashboard.models import CxC, PlanCortoPlazo
from dashboard.forms.cxc_form import CxCRegisterForm
import pandas as pd
import numpy as np


def cxc_list(request):
    datos = CxC.objects.all()
    return render(request, 'dashboard/cxc_list.html', {'datos': datos})


def cxc_register(request):
    if request.method == 'POST':
        form = CxCRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:cxc_list')
        else:
            return render(request, 'dashboard/cxc_register.html', {'form': form})
    else:
        form = CxCRegisterForm()
        return render(request, 'dashboard/cxc_register.html', {'form': form})


def cxc_import(request):
    if request.method == 'POST':

        try:
            df = pd.read_excel(request.FILES['file'])

            # Nombres del archivo y los de la BD
            dict_nombres = {
                'col1':'representante_proyecto',
                'col2':'proyecto',
                'col3':'clasificacion_planta',
                'col4':'oef_asignada',
                'col5':'inicio_vigencia',
                'col6':'fin_vigencia',
                'col7':'tecnologia',
                'col8':'capacidad',
                'col9':'fecha_entrada'
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
            df['inicio_vigencia'] = pd.to_datetime(df['inicio_vigencia'], format="%Y/%m/%d")
            df['fin_vigencia'] = pd.to_datetime(df['fin_vigencia'], format="%Y/%m/%d")
            df['fecha_entrada'] = pd.to_datetime(df['fecha_entrada'], format="%Y/%m/%d")

            # Convertir toda los datos de la df a str para poder realizar la insercion en la bd
            df = df.astype(str)

            # Reemplazar los datos vacios o guiones en None's para realizar la insercion en la bd
            df.replace(to_replace=["nan", " - ", "NaT"], value=[None, None, None], inplace=True)

            # Borrar todos los datos de la tabla para realizar la nueva insercion
            CxC.objects.all().delete()

            for index, row in df.iterrows():
                instance = CxC(
                    representante_proyecto=row[0],
                    proyecto=row[1],
                    clasificacion_planta=row[2],
                    oef_asignada=row[3],
                    inicio_vigencia=row[4],
                    fin_vigencia=row[5],
                    tecnologia=row[6],
                    capacidad=row[7],
                    fecha_entrada=row[8]
                )
                instance.save()
                print(row[0])
                print(row[1])
                print(row[2])
                print(row[3])
                print(row[4])
                print(row[5])
                print(row[6])
                print(row[7])
                print(row[8])
                print('-------')

        except Exception as e:
            print(e)

        return redirect('dashboard:demcarac_list')
    else:
        return render(request, 'dashboard/import_file.html')


def cxc_edit(request, id):
    form = None
    error = None
    try:
        cxc = CxC.objects.get(id = id)
        if request.method == 'GET':
            form = CxCRegisterForm(instance = cxc)
        else:
            form = CxCRegisterForm(request.POST, instance = cxc)
            if form.is_valid():
                plan_corto_plazo = PlanCortoPlazo.objects.filter(planta = cxc.proyecto).first()

                cxc.fecha_entrada = None
                if plan_corto_plazo is not None:
                    cxc.fecha_entrada = plan_corto_plazo.fecha

                form.save()
                return redirect('dashboard:cxc_list')

    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'dashboard/cxc_register.html', {'form': form, 'error': error})
