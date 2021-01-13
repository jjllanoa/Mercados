from django.urls import path
from dashboard.views import (
    auth,
    user,
    dashboard,
    plan_energia_firme_demanda,
    plan_corto_plazo,
    plan_meta_matriz_ernc,
    plan_capacidad_adicional_max_ernc,
    plan_meta_matriz,
    plan_capacidad_adicional_max,
    demcarac,
    meta_matriz,
    capmax,
    dentradatec,
    demenficc_fil,
    lcoe,
    matriz_actual,
    demanda,
    planta,
    cxc,
    clp,
    consolidado_existente,
    regresiones,
    crecimiento_mw,
    existente_cxc_clp,
    adicional,
)

urlpatterns = [
    # auth.py - OK
    path('login/', auth.log_in, name = 'login'),
    path('logout/', auth.log_out, name = 'logout'),

    # user.py - delete
    path('user_list/', user.user_list, name = 'user_list'),
    path('user_register/', user.user_register, name = 'user_register'),
    path('user_edit/<int:id>', user.user_edit, name = 'user_edit'),
    path('user_delete/<int:id>', user.user_delete, name = 'user_delete'),

    # dashboard.py
    path('', dashboard.index, name = 'index'),

    # plan_energia_firme_demanda.py - OK
    path('plan_energia_firme_demanda_list/', plan_energia_firme_demanda.plan_energia_firme_demanda_list, name = 'plan_energia_firme_demanda_list'),
    path('plan_energia_firme_demanda_edit/<int:id>', plan_energia_firme_demanda.plan_energia_firme_demanda_edit, name = 'plan_energia_firme_demanda_edit'),

    # plan_corto_plazo.py - delete
    path('plan_corto_plazo_list/', plan_corto_plazo.plan_corto_plazo_list, name = 'plan_corto_plazo_list'),
    path('plan_corto_plazo_register/', plan_corto_plazo.plan_corto_plazo_register, name = 'plan_corto_plazo_register'),
    path('plan_corto_plazo_edit/<int:id>', plan_corto_plazo.plan_corto_plazo_edit, name = 'plan_corto_plazo_edit'),

    # plan_meta_matriz_ernc.py - delete
    path('plan_meta_matriz_ernc_list/', plan_meta_matriz_ernc.plan_meta_matriz_ernc_list, name = 'plan_meta_matriz_ernc_list'),
    path('plan_meta_matriz_ernc_register/', plan_meta_matriz_ernc.plan_meta_matriz_ernc_register, name = 'plan_meta_matriz_ernc_register'),
    path('plan_meta_matriz_ernc_edit/<int:id>', plan_meta_matriz_ernc.plan_meta_matriz_ernc_edit, name = 'plan_meta_matriz_ernc_edit'),

    # plan_capacidad_adicional_max_ernc.py - delete
    path('plan_capacidad_adicional_max_ernc_list/', plan_capacidad_adicional_max_ernc.plan_capacidad_adicional_max_ernc_list, name = 'plan_capacidad_adicional_max_ernc_list'),
    path('plan_capacidad_adicional_max_ernc_register/', plan_capacidad_adicional_max_ernc.plan_capacidad_adicional_max_ernc_register, name = 'plan_capacidad_adicional_max_ernc_register'),
    path('plan_capacidad_adicional_max_ernc_edit/<int:id>', plan_capacidad_adicional_max_ernc.plan_capacidad_adicional_max_ernc_edit, name = 'plan_capacidad_adicional_max_ernc_edit'),

    # plan_meta_matriz.py - delete
    path('plan_meta_matriz_list/', plan_meta_matriz.plan_meta_matriz_list, name = 'plan_meta_matriz_list'),
    path('plan_meta_matriz_register/', plan_meta_matriz.plan_meta_matriz_register, name = 'plan_meta_matriz_register'),
    path('plan_meta_matriz_edit/<int:id>', plan_meta_matriz.plan_meta_matriz_edit, name = 'plan_meta_matriz_edit'),

    # plan_capacidad_adicional_max.py - delete
    path('plan_capacidad_adicional_max_list/', plan_capacidad_adicional_max.plan_capacidad_adicional_max_list, name = 'plan_capacidad_adicional_max_list'),
    path('plan_capacidad_adicional_max_register/', plan_capacidad_adicional_max.plan_capacidad_adicional_max_register, name = 'plan_capacidad_adicional_max_register'),
    path('plan_capacidad_adicional_max_edit/<int:id>', plan_capacidad_adicional_max.plan_capacidad_adicional_max_edit, name = 'plan_capacidad_adicional_max_edit'),

    # demcarac.py - organizar
    path('demcarac_list/', demcarac.demcarac_list, name = 'demcarac_list'),
    path('demcarac_register/', demcarac.demcarac_register, name = 'demcarac_register'),
    path('demcarac_import/', demcarac.demcarac_import, name = 'demcarac_import'),
    path('demcarac_edit/<int:id>', demcarac.demcarac_edit, name = 'demcarac_edit'),
    path('demcarac_delete/<int:id>', demcarac.demcarac_delete, name = 'demcarac_delete'),

    # meta_matriz.py - delete
    path('meta_matriz_list/', meta_matriz.meta_matriz_list, name = 'meta_matriz_list'),
    path('meta_matriz_register/', meta_matriz.meta_matriz_register, name = 'meta_matriz_register'),
    path('meta_matriz_edit/<int:id>', meta_matriz.meta_matriz_edit, name = 'meta_matriz_edit'),

    # capmax.py - delete
    path('capmax_list/', capmax.capmax_list, name = 'capmax_list'),
    path('capmax_register/', capmax.capmax_register, name = 'capmax_register'),
    path('capmax_edit/<int:id>', capmax.capmax_edit, name = 'capmax_edit'),

    # dentradatec.py - delete
    path('dentradatec_list/', dentradatec.dentradatec_list, name = 'dentradatec_list'),
    path('dentradatec_register/', dentradatec.dentradatec_register, name = 'dentradatec_register'),
    path('dentradatec_edit/<int:id>', dentradatec.dentradatec_edit, name = 'dentradatec_edit'),

    # demenficc_fil.py - delete
    path('demenficc_fil_list/', demenficc_fil.demenficc_fil_list, name = 'demenficc_fil_list'),
    path('demenficc_fil_register/', demenficc_fil.demenficc_fil_register, name = 'demenficc_fil_register'),
    path('demenficc_fil_edit/<int:id>', demenficc_fil.demenficc_fil_edit, name = 'demenficc_fil_edit'),

    # lcoe.py - delete
    path('lcoe_list/', lcoe.lcoe_list, name = 'lcoe_list'),
    path('lcoe_register/', lcoe.lcoe_register, name = 'lcoe_register'),
    path('lcoe_edit/<int:id>', lcoe.lcoe_edit, name = 'lcoe_edit'),

    # matriz_actual.py - edit, delete, list de matriz actual ndc
    path('matriz_actual_list/', matriz_actual.matriz_actual_list, name = 'matriz_actual_list'),
    path('matriz_actual_dc_register/', matriz_actual.matriz_actual_dc_register, name = 'matriz_actual_dc_register'),
    path('matriz_actual_dc_import/', matriz_actual.matriz_actual_dc_import, name = 'matriz_actual_dc_import'),
    path('matriz_actual_ndc_register/', matriz_actual.matriz_actual_ndc_register, name = 'matriz_actual_ndc_register'),

    # demanda.py - delete, operación en campos
    path('demanda_list/', demanda.demanda_list, name = 'demanda_list'),
    path('demanda_register/', demanda.demanda_register, name = 'demanda_register'),
    path('demanda_import/', demanda.demanda_import, name = 'demanda_import'),
    path('demanda_edit/<int:id>', demanda.demanda_edit, name = 'demanda_edit'),

    # planta.py - delete
    path('planta_list/', planta.planta_list, name = 'planta_list'),
    path('planta_register/', planta.planta_register, name = 'planta_register'),
    path('planta_import/', planta.planta_import, name = 'planta_import'),
    path('planta_edit/<int:id>', planta.planta_edit, name = 'planta_edit'),

    # cxc.py - delete
    path('cxc_list/', cxc.cxc_list, name = 'cxc_list'),
    path('cxc_register/', cxc.cxc_register, name = 'cxc_register'),
    path('cxc_edit/<int:id>', cxc.cxc_edit, name = 'cxc_edit'),

    # clp.py - delete, operación en campos
    path('clp_list/', clp.clp_list, name = 'clp_list'),
    path('clp_register/', clp.clp_register, name = 'clp_register'),
    # path('clp_edit/<int:id>', clp.clp_edit, name = 'clp_edit'),

    # consolidado_existente.py - delete
    path('consolidado_existente_list/', consolidado_existente.consolidado_existente_list, name = 'consolidado_existente_list'),
    path('consolidado_existente_register/', consolidado_existente.consolidado_existente_register, name = 'consolidado_existente_register'),
    path('consolidado_existente_edit/<int:id>', consolidado_existente.consolidado_existente_edit, name = 'consolidado_existente_edit'),

    path('regresiones_register/', regresiones.regresiones_register, name = 'regresiones_register'),

    # crecimiento_mw.py - delete
    path('crecimiento_mw_list/', crecimiento_mw.crecimiento_mw_list, name = 'crecimiento_mw_list'),
    path('crecimiento_mw_register/', crecimiento_mw.crecimiento_mw_register, name = 'crecimiento_mw_register'),
    path('crecimiento_mw_edit/<int:id>', crecimiento_mw.crecimiento_mw_edit, name = 'crecimiento_mw_edit'),

    # existente_cxc_clp.py - delete
    path('existente_cxc_clp_list/', existente_cxc_clp.existente_cxc_clp_list, name = 'existente_cxc_clp_list'),
    path('existente_cxc_clp_register/', existente_cxc_clp.existente_cxc_clp_register, name = 'existente_cxc_clp_register'),
    path('existente_cxc_clp_edit/<int:id>', existente_cxc_clp.existente_cxc_clp_edit, name = 'existente_cxc_clp_edit'),

    # adicional.py - delete
    path('adicional_list/', adicional.adicional_list, name = 'adicional_list'),
    path('adicional_register/', adicional.adicional_register, name = 'adicional_register'),
    path('adicional_edit/<int:id>', adicional.adicional_edit, name = 'adicional_edit'),
]