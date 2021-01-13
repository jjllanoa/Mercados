from django.db import models
# from django.core.validators import MaxLengthValidator

# Create your models here.
class DemCarac(models.Model):
    bloque = models.DecimalField('Bloque', max_digits=3, decimal_places=0, blank=False, null=False)
    duracion = models.DecimalField('Duración', max_digits=5, decimal_places=4, blank=False, null=False)
    restup = models.DecimalField('Restup', max_digits=5, decimal_places=4, blank=False, null=False)
    restdn = models.DecimalField('Restdn', max_digits=5, decimal_places=4, blank=False, null=False)

    class Meta:
        verbose_name = 'DemCarac'
        ordering = ['bloque']

    def __str__(self):
        return self.bloque


class MatrizActualDC(models.Model):
    tipo = models.CharField('Tipo', max_length=100, blank=False, null=False)
    capacidad = models.DecimalField('Capacidad', max_digits=10, decimal_places=5, blank=False, null=False)
    conversion = models.DecimalField('Conversión', max_digits=10, decimal_places=5, blank=True, null=True)
    fecha = models.DateField('Fecha', auto_now=False, auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name = 'MatrizActualDC'
        ordering = ['id']

    def __str__(self):
        return self.tipo


class MatrizActualNDC(models.Model):
    tipo = models.CharField('Tipo', max_length=100, blank=False, null=False)
    capacidad = models.DecimalField('Capacidad', max_digits=10, decimal_places=5, blank=False, null=False)
    conversion = models.DecimalField('Conversión', max_digits=10, decimal_places=5, blank=True, null=True)
    fecha = models.DateField('Fecha', auto_now=False, auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name = 'MatrizActualNDC'
        ordering = ['id']

    def __str__(self):
        return self.tipo


class Demanda(models.Model):
    fecha = models.DateField('Fecha', auto_now=False, auto_now_add=False, blank=True, null=True)
    dia_mes = models.IntegerField('Día mes', blank=False, null=False)
    demanda_energia = models.DecimalField('Demanda energía', max_digits=10, decimal_places=5, blank=False, null=False)
    demanda_energia_dia = models.DecimalField('Demanda energía día', max_digits=10, decimal_places=5, blank=True, null=True)

    # @property
    # def get_division(self):
    #     return (self.demanda_energia / self.dia_mes)

    # def Save(self):
    #     self.demanda_energia_dia = (self.demanda_energia / self.dia_mes)
    #     super (Demanda, self).save()

    class Meta:
        verbose_name = 'Demanda'
        ordering = ['fecha']

    def __str__(self):
        return self.fecha


class Planta(models.Model):
    agente = models.CharField('Agente', max_length=100, blank=False, null=False)
    planta = models.CharField('Planta', max_length=100, blank=False, null=False)
    tipo = models.CharField('Tipo', max_length=10, blank=False, null=False)
    dc_ndc = models.CharField('DC NDC', max_length=10, blank=False, null=False)
    clasificacion = models.CharField('Clasificación', max_length=10, blank=False, null=False)
    contrato = models.CharField('Contrato', max_length=10, blank=True, null=True)
    enficc_verificada = models.DecimalField('ENFICC verificada', max_digits=10, decimal_places=2, blank=True, null=True)
    enficc_no_comprometida = models.DecimalField('ENFICC no comprometida', max_digits=10, decimal_places=2, blank=True, null=True)
    fecha_inicio_vigencia_enficc = models.DateField('Fecha inicio vigencia ENFICC', auto_now=False, auto_now_add=False, blank=True, null=True)
    fecha_fin_vigencia_enficc = models.DateField('Fecha fin vigencia ENFICC', auto_now=False, auto_now_add=False, blank=True, null=True)
    combustible_declarado = models.CharField('Combustible declarado', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Planta'
        ordering = ['agente']

    def __str__(self):
        return self.agente


class CxC(models.Model):
    representante_proyecto = models.CharField('Representante del proyecto', max_length=100, blank=False, null=False)
    proyecto = models.CharField('Proyecto', max_length=100, blank=False, null=False)
    clasificacion_planta = models.CharField('Clasificación de la planta', max_length=50, blank=False, null=False)
    oef_asignada = models.DecimalField('OEF asignada', max_digits=10, decimal_places=2, blank=False, null=False)
    inicio_vigencia = models.DateField('Inicio vigencia', auto_now=False, auto_now_add=False, blank=False, null=False)
    fin_vigencia = models.DateField('Fin vigencia', auto_now=False, auto_now_add=False, blank=False, null=False)
    tecnologia = models.CharField('Tecnología', max_length=50, blank=False, null=False)
    capacidad = models.DecimalField('Capacidad instalada', max_digits=5, decimal_places=2, blank=False, null=False)
    fecha_entrada = models.DateField('Fecha entrada', auto_now=False, auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name = 'CxC'
        ordering = ['representante_proyecto']

    def __str__(self):
        return self.representante_proyecto


class CLP(models.Model):
    representante_proyecto = models.CharField('Representante del proyecto', max_length=100, blank=True, null=True)
    proyecto = models.CharField('Proyecto', max_length=100, blank=False, null=False)
    clasificacion_planta = models.CharField('Clasificación de la planta', max_length=50, blank=False, null=False)
    oef_asignada = models.DecimalField('OEF asignada', max_digits=10, decimal_places=1, blank=True, null=True)
    inicio_vigencia = models.DateField('Inicio vigencia', auto_now=False, auto_now_add=False, blank=True, null=True)
    fin_vigencia = models.DateField('Fin vigencia', auto_now=False, auto_now_add=False, blank=True, null=True)
    tecnologia = models.CharField('Tecnología', max_length=50, blank=False, null=False)
    capacidad = models.DecimalField('Capacidad instalada', max_digits=5, decimal_places=2, blank=False, null=False)
    fecha_entrada = models.DateField('Fecha entrada', auto_now=False, auto_now_add=False, blank=True, null=True)

    class Meta:
        verbose_name = 'CLP'
        ordering = ['representante_proyecto']

    def __str__(self):
        return self.representante_proyecto


class ConsolidadoExistente(models.Model):
    fuente_energia = models.CharField('Fuente de energía', max_length=100, blank=False, null=False)
    planta = models.CharField('planta', max_length=100, blank=True, null=True)
    capacidad = models.DecimalField('Capacidad', max_digits=10, decimal_places=2, blank=True, null=True)
    enficc = models.DecimalField('ENFICC', max_digits=10, decimal_places=1, blank=True, null=True)
    tipo = models.CharField('Tipo', max_length=50, blank=False, null=False)
    asignacion = models.CharField('Asignación', max_length=250, blank=True, null=True)

    class Meta:
        verbose_name = 'ConsolidadoExistente'
        ordering = ['fuente_energia']

    def __str__(self):
        return self.fuente_energia


class CrecimientoMW(models.Model):
    fecha = models.DateField('Fecha', auto_now=False, auto_now_add=False, blank=False, null=False)
    hidraulica = models.DecimalField('Hidráulica', max_digits=8, decimal_places=2, blank=True, null=True)
    liquidos = models.DecimalField('Liquidos', max_digits=8, decimal_places=2, blank=True, null=True)
    carbon = models.DecimalField('Carbon', max_digits=8, decimal_places=2, blank=True, null=True)
    gas = models.DecimalField('Gas', max_digits=8, decimal_places=2, blank=True, null=True)
    glp = models.DecimalField('GLP', max_digits=8, decimal_places=2, blank=True, null=True)
    pch = models.DecimalField('PCH', max_digits=8, decimal_places=2, blank=True, null=True)
    ndc_t = models.DecimalField('NDC_T', max_digits=8, decimal_places=2, blank=True, null=True)
    solar = models.DecimalField('Solar', max_digits=8, decimal_places=2, blank=True, null=True)
    eolica = models.DecimalField('Eolica', max_digits=8, decimal_places=2, blank=True, null=True)
    total = models.DecimalField('Total', max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'CrecimientoMW'
        ordering = ['fecha']

    def __str__(self):
        return self.fecha


class ExistenteCxCCLP(models.Model):
    fecha = models.DateField('Fecha', auto_now=False, auto_now_add=False, blank=False, null=False)
    hidraulica = models.DecimalField('Hidráulica', max_digits=6, decimal_places=2, blank=True, null=True)
    liquidos = models.DecimalField('Liquidos', max_digits=6, decimal_places=2, blank=True, null=True)
    carbon = models.DecimalField('Carbon', max_digits=6, decimal_places=2, blank=True, null=True)
    gas = models.DecimalField('Gas', max_digits=6, decimal_places=2, blank=True, null=True)
    glp = models.DecimalField('GLP', max_digits=6, decimal_places=2, blank=True, null=True)
    pch = models.DecimalField('PCH', max_digits=6, decimal_places=2, blank=True, null=True)
    ndc_t = models.DecimalField('NDC_T', max_digits=6, decimal_places=2, blank=True, null=True)
    solar = models.DecimalField('Solar', max_digits=6, decimal_places=2, blank=True, null=True)
    eolica = models.DecimalField('Eolica', max_digits=6, decimal_places=2, blank=True, null=True)
    existente_cxc_clp = models.DecimalField('Existente CxC CLP', max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'ExistenteCxCCLP'
        ordering = ['fecha']

    def __str__(self):
        return self.fecha


class Adicional(models.Model):
    fecha = models.DateField('Fecha', auto_now=False, auto_now_add=False, blank=False, null=False)
    hidraulica = models.DecimalField('Hidráulica', max_digits=6, decimal_places=2, blank=True, null=True)
    liquidos = models.DecimalField('Liquidos', max_digits=6, decimal_places=2, blank=True, null=True)
    carbon = models.DecimalField('Carbon', max_digits=6, decimal_places=2, blank=True, null=True)
    gas = models.DecimalField('Gas', max_digits=6, decimal_places=2, blank=True, null=True)
    glp = models.DecimalField('GLP', max_digits=6, decimal_places=2, blank=True, null=True)
    pch = models.DecimalField('PCH', max_digits=6, decimal_places=2, blank=True, null=True)
    ndc_t = models.DecimalField('NDC_T', max_digits=6, decimal_places=2, blank=True, null=True)
    solar = models.DecimalField('Solar', max_digits=6, decimal_places=2, blank=True, null=True)
    eolica = models.DecimalField('Eolica', max_digits=6, decimal_places=2, blank=True, null=True)
    expansion_adicional = models.DecimalField('Expansión adicional', max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'Adicional'
        ordering = ['fecha']

    def __str__(self):
        return self.fecha


class PlanEnergiaFirmeDemanda(models.Model):
    fecha_inicial = models.IntegerField('Fecha inicial', blank=False, null=False)
    fecha_final = models.IntegerField('Fecha final', blank=False, null=False)
    periodicidad_subasta = models.IntegerField('Periodicidad subasta', blank=False, null=False)

    class Meta:
        verbose_name = 'PlanEnergiaFirmeDemanda'
        ordering = ['fecha_inicial']

    def __str__(self):
        return self.fecha_inicial


class PlanCortoPlazo(models.Model):
    planta = models.CharField('Planta', max_length=100, blank=False, null=False)
    fecha = models.DateField('Fecha', auto_now=False, auto_now_add=False, blank=False, null=False)
    tipo = models.CharField('Tipo', max_length=100, blank=False, null=False)
    asignacion = models.CharField('Asignación', max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'PlanCortoPlazo'
        ordering = ['planta']

    def __str__(self):
        return self.planta


class PlanMetaMatrizERNC(models.Model):
    fecha = models.IntegerField('Fecha', blank=False, null=False)
    eolica = models.DecimalField('Eolica', max_digits=5, decimal_places=1, blank=True, null=True)
    solar = models.DecimalField('Solar', max_digits=5, decimal_places=1, blank=True, null=True)
    pch = models.DecimalField('PCH', max_digits=5, decimal_places=1, blank=True, null=True)
    ndc_t = models.DecimalField('NDC_T', max_digits=5, decimal_places=1, blank=True, null=True)
    ernc = models.DecimalField('ERNC', max_digits=5, decimal_places=1, blank=True, null=True)

    class Meta:
        verbose_name = 'PlanMetaMatrizERNC'
        ordering = ['fecha']

    def __str__(self):
        return self.fecha


class PlanCapacidadAdicionalMaxERNC(models.Model):
    fecha = models.IntegerField('Fecha', blank=False, null=False)
    eolica = models.DecimalField('Eolica', max_digits=10, decimal_places=2, blank=True, null=True)
    solar = models.DecimalField('Solar', max_digits=10, decimal_places=2, blank=True, null=True)
    pch = models.DecimalField('PCH', max_digits=10, decimal_places=2, blank=True, null=True)
    ndc_t = models.DecimalField('NDC_T', max_digits=10, decimal_places=2, blank=True, null=True)
    ernc = models.DecimalField('ERNC', max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'PlanCapacidadAdicionalMaxERNC'
        ordering = ['fecha']

    def __str__(self):
        return self.fecha


class PlanMetaMatriz(models.Model):
    fecha = models.IntegerField('Fecha', blank=False, null=False)
    liquidos = models.DecimalField('Liquidos', max_digits=5, decimal_places=1, blank=True, null=True)
    carbon = models.DecimalField('Carbon', max_digits=5, decimal_places=1, blank=True, null=True)
    gas = models.DecimalField('Gas', max_digits=5, decimal_places=1, blank=True, null=True)
    glp = models.DecimalField('GLP', max_digits=5, decimal_places=1, blank=True, null=True)
    hidraulica = models.DecimalField('Hidráulica', max_digits=5, decimal_places=1, blank=True, null=True)

    class Meta:
        verbose_name = 'PlanMetaMatriz'
        ordering = ['fecha']

    def __str__(self):
        return self.fecha
        # return str(self.fecha)


class PlanCapacidadAdicionalMax(models.Model):
    fecha = models.IntegerField('Fecha', blank=False, null=False)
    liquidos = models.DecimalField('Liquidos', max_digits=10, decimal_places=2, blank=True, null=True)
    carbon = models.DecimalField('Carbon', max_digits=10, decimal_places=2, blank=True, null=True)
    gas = models.DecimalField('Gas', max_digits=10, decimal_places=2, blank=True, null=True)
    glp = models.DecimalField('GLP', max_digits=10, decimal_places=2, blank=True, null=True)
    hidraulica = models.DecimalField('Hidráulica', max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = 'PlanCapacidadAdicionalMax'
        ordering = ['fecha']

    def __str__(self):
        return self.fecha


class MetaMatriz(models.Model):
    fecha = models.IntegerField('Fecha', blank=False, null=False)
    hidraulica = models.DecimalField('Hidráulica', max_digits=6, decimal_places=4, blank=False, null=False)
    liquidos = models.DecimalField('Liquidos', max_digits=6, decimal_places=4, blank=False, null=False)
    carbon = models.DecimalField('Carbon', max_digits=6, decimal_places=4, blank=False, null=False)
    gas = models.DecimalField('Gas', max_digits=6, decimal_places=4, blank=False, null=False)
    glp = models.DecimalField('GLP', max_digits=6, decimal_places=4, blank=False, null=False)
    pch = models.DecimalField('PCH', max_digits=6, decimal_places=4, blank=False, null=False)
    ndc_t = models.DecimalField('NDC_T', max_digits=6, decimal_places=4, blank=False, null=False)
    solar = models.DecimalField('Solar', max_digits=6, decimal_places=4, blank=False, null=False)
    eolica = models.DecimalField('Eolica', max_digits=6, decimal_places=4, blank=False, null=False)

    class Meta:
        verbose_name = 'MetaMatriz'
        ordering = ['fecha']

    def __str__(self):
        return self.fecha


class CapMax(models.Model):
    fecha = models.IntegerField('Fecha', blank=False, null=False)
    hidraulica = models.DecimalField('Hidráulica', max_digits=10, decimal_places=2, blank=False, null=False)
    liquidos = models.DecimalField('Liquidos', max_digits=10, decimal_places=2, blank=False, null=False)
    carbon = models.DecimalField('Carbon', max_digits=10, decimal_places=2, blank=False, null=False)
    gas = models.DecimalField('Gas', max_digits=10, decimal_places=2, blank=False, null=False)
    glp = models.DecimalField('GLP', max_digits=10, decimal_places=2, blank=False, null=False)
    pch = models.DecimalField('PCH', max_digits=10, decimal_places=2, blank=False, null=False)
    ndc_t = models.DecimalField('NDC_T', max_digits=10, decimal_places=2, blank=False, null=False)
    solar = models.DecimalField('Solar', max_digits=10, decimal_places=2, blank=False, null=False)
    eolica = models.DecimalField('Eolica', max_digits=10, decimal_places=2, blank=False, null=False)

    class Meta:
        verbose_name = 'CapMax'
        ordering = ['fecha']

    def __str__(self):
        return self.fecha


class DEntradaTec(models.Model):
    variable = models.CharField('Variable', max_length=100, blank=False, null=False)
    hidraulica = models.DecimalField('Hidráulica', max_digits=7, decimal_places=2, blank=False, null=False)
    liquidos = models.DecimalField('Liquidos', max_digits=7, decimal_places=2, blank=False, null=False)
    carbon = models.DecimalField('Carbon', max_digits=7, decimal_places=2, blank=False, null=False)
    gas = models.DecimalField('Gas', max_digits=7, decimal_places=2, blank=False, null=False)
    glp = models.DecimalField('GLP', max_digits=7, decimal_places=2, blank=False, null=False)
    pch = models.DecimalField('PCH', max_digits=7, decimal_places=2, blank=False, null=False)
    ndc_t = models.DecimalField('NDC_T', max_digits=7, decimal_places=2, blank=False, null=False)
    solar = models.DecimalField('Solar', max_digits=7, decimal_places=2, blank=False, null=False)
    eolica = models.DecimalField('Eolica', max_digits=7, decimal_places=2, blank=False, null=False)

    class Meta:
        verbose_name = 'DEntradaTec'
        ordering = ['variable']

    def __str__(self):
        return self.variable


# class DEntradaGen(models.Model):


# class FechaCP(models.Model):


class DemENFICCFil(models.Model):
    fecha = models.DateField('Fecha', auto_now=False, auto_now_add=False, blank=False, null=False)
    demanda_energia = models.DecimalField('Demanda energía', max_digits=10, decimal_places=4, blank=False, null=False)
    enficc = models.DecimalField('ENFICC', max_digits=10, decimal_places=5, blank=False, null=False)

    class Meta:
        verbose_name = 'DemENFICCFil'
        ordering = ['fecha']

    def __str__(self):
        return self.fecha


class LCOE(models.Model):
    fecha = models.IntegerField('Fecha', blank=False, null=False)
    hidraulica = models.DecimalField('Hidráulica', max_digits=5, decimal_places=2, blank=False, null=False)
    liquidos = models.DecimalField('Liquidos', max_digits=5, decimal_places=2, blank=False, null=False)
    carbon = models.DecimalField('Carbon', max_digits=5, decimal_places=2, blank=False, null=False)
    gas = models.DecimalField('Gas', max_digits=5, decimal_places=2, blank=False, null=False)
    glp = models.DecimalField('GLP', max_digits=5, decimal_places=2, blank=False, null=False)
    pch = models.DecimalField('PCH', max_digits=5, decimal_places=2, blank=False, null=False)
    ndc_t = models.DecimalField('NDC_T', max_digits=5, decimal_places=2, blank=False, null=False)
    solar = models.DecimalField('Solar', max_digits=5, decimal_places=2, blank=False, null=False)
    eolica = models.DecimalField('Eolica', max_digits=5, decimal_places=2, blank=False, null=False)

    class Meta:
        verbose_name = 'LCOE'
        ordering = ['fecha']

    def __str__(self):
        return self.fecha


class RegresionMetaMatriz(models.Model):
    fecha = models.IntegerField('Fecha', blank=False, null=False)
    eolica = models.DecimalField('Eolica', max_digits=5, decimal_places=2, blank=False, null=False)
    solar = models.DecimalField('Solar', max_digits=5, decimal_places=2, blank=False, null=False)
    pch = models.DecimalField('PCH', max_digits=5, decimal_places=2, blank=False, null=False)
    ndc_t = models.DecimalField('NDC_T', max_digits=5, decimal_places=2, blank=False, null=False)
    ernc = models.DecimalField('ERNC', max_digits=5, decimal_places=2, blank=False, null=False)
    liquidos = models.DecimalField('Liquidos', max_digits=5, decimal_places=2, blank=False, null=False)
    carbon = models.DecimalField('Carbon', max_digits=5, decimal_places=2, blank=False, null=False)
    gas = models.DecimalField('Gas', max_digits=5, decimal_places=2, blank=False, null=False)
    glp = models.DecimalField('GLP', max_digits=5, decimal_places=2, blank=False, null=False)
    termica = models.DecimalField('PCH', max_digits=5, decimal_places=2, blank=False, null=False)
    hidraulica = models.DecimalField('Hidráulica', max_digits=5, decimal_places=2, blank=False, null=False)

    class Meta:
        verbose_name = 'RegresionMetaMatriz'
        ordering = ['fecha']

    def __str__(self):
        return self.fecha


# class RegresionPotenciaI():
#     pass
