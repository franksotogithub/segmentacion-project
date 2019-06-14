from django.db import models

# Create your models here.

class Departamento(models.Model):
    ccdd = models.CharField(db_column='CCDD', max_length=2,primary_key=True)  # Field name made lowercase.
    cant_prov_marco = models.IntegerField(db_column='CANT_PROV_MARCO', blank=True, null=True)  # Field name made lowercase.
    cant_prov_segm = models.IntegerField(db_column='CANT_PROV_SEGM', blank=True, null=True)  # Field name made lowercase.
    flag_segm = models.IntegerField(db_column='FLAG_SEGM', blank=True, null=True)  # Field name made lowercase.
    porcent_segm = models.DecimalField(db_column='PORCENT_SEGM', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fase = models.CharField(db_column='FASE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #id = models.IntegerField(db_column='ID',blank=True,null=True)  # Field name made lowercase.
    cant_dist_marco = models.IntegerField(db_column='CANT_DIST_MARCO', blank=True, null=True)  # Field name made lowercase.
    cant_dist_segm = models.IntegerField(db_column='CANT_DIST_SEGM', blank=True, null=True)  # Field name made lowercase.
    cant_zonas_marco = models.IntegerField(db_column='CANT_ZONAS_MARCO', blank=True, null=True)  # Field name made lowercase.
    cant_zonas_segm = models.IntegerField(db_column='CANT_ZONAS_SEGM', blank=True, null=True)  # Field name made lowercase.
    cant_secc_u = models.IntegerField(db_column='CANT_SECC_U', blank=True, null=True)  # Field name made lowercase.
    cant_ae_u = models.IntegerField(db_column='CANT_AE_U', blank=True, null=True)  # Field name made lowercase.
    cant_secc_r = models.IntegerField(db_column='CANT_SECC_R', blank=True, null=True)  # Field name made lowercase.
    cant_ae_r = models.IntegerField(db_column='CANT_AE_R', blank=True, null=True)  # Field name made lowercase.
    nombdep = models.CharField(db_column='NOMBDEP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    porcent_segm_calidad = models.DecimalField(db_column='PORCENT_SEGM_CALIDAD', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = False
        db_table = 'marco_departamentos'

class Provincia(models.Model):
    codprov = models.CharField(db_column='CODPROV', max_length=4,primary_key=True)  # Field name made lowercase.
    ccdd = models.ForeignKey(Departamento,db_column='CCDD',on_delete=False,blank=True,null=True)
    ccpp = models.CharField(db_column='CCPP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cant_dist_marco = models.IntegerField(db_column='CANT_DIST_MARCO', blank=True, null=True)  # Field name made lowercase.
    cant_dist_segm = models.IntegerField(db_column='CANT_DIST_SEGM', blank=True, null=True)  # Field name made lowercase.
    flag_segm = models.IntegerField(db_column='FLAG_SEGM', blank=True, null=True)  # Field name made lowercase.
    porcent_segm = models.DecimalField(db_column='PORCENT_SEGM', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    fase = models.CharField(db_column='FASE', max_length=25, blank=True, null=True)  # Field name made lowercase.
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    cant_zonas_marco = models.IntegerField(db_column='CANT_ZONAS_MARCO', blank=True, null=True)  # Field name made lowercase.
    cant_zonas_segm = models.IntegerField(db_column='CANT_ZONAS_SEGM', blank=True, null=True)  # Field name made lowercase.
    cant_secc_u = models.IntegerField(db_column='CANT_SECC_U', blank=True, null=True)  # Field name made lowercase.
    cant_ae_u = models.IntegerField(db_column='CANT_AE_U', blank=True, null=True)  # Field name made lowercase.
    cant_secc_r = models.IntegerField(db_column='CANT_SECC_R', blank=True, null=True)  # Field name made lowercase.
    cant_ae_r = models.IntegerField(db_column='CANT_AE_R', blank=True, null=True)  # Field name made lowercase.
    nombprov = models.CharField(db_column='NOMBPROV', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iddepope = models.CharField(db_column='IDDEPOPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    porcent_segm_calidad = models.DecimalField(db_column='PORCENT_SEGM_CALIDAD', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nombdep = models.CharField(db_column='NOMBDEP', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = True
        db_table = 'marco_provincias'


class Distrito(models.Model):
    ubigeo = models.CharField(db_column='UBIGEO', max_length=6,primary_key=True)  # Field name made lowercase.
    ccdd = models.CharField(db_column='CCDD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nombdep = models.CharField(db_column='NOMBDEP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ccpp = models.CharField(db_column='CCPP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nombprov = models.CharField(db_column='NOMBPROV', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ccdi = models.CharField(db_column='CCDI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nombdist = models.CharField(db_column='NOMBDIST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    capital = models.CharField(db_column='CAPITAL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    codprov = models.ForeignKey(Provincia,db_column='CODPROV',on_delete=False,blank=True,null=True)
    cant_zonas_marco = models.IntegerField(db_column='CANT_ZONAS_MARCO', blank=True, null=True)  # Field name made lowercase.
    cant_zonas_segm = models.IntegerField(db_column='CANT_ZONAS_SEGM', blank=True, null=True)  # Field name made lowercase.
    id_estrato = models.IntegerField(db_column='ID_ESTRATO', blank=True, null=True)  # Field name made lowercase.
    prioridad = models.IntegerField(db_column='PRIORIDAD', blank=True, null=True)  # Field name made lowercase.
    flag_segm = models.IntegerField(db_column='FLAG_SEGM', blank=True, null=True)  # Field name made lowercase.
    flag_segm_u = models.IntegerField(db_column='FLAG_SEGM_U', blank=True, null=True)  # Field name made lowercase.
    flag_segm_r = models.IntegerField(db_column='FLAG_SEGM_R', blank=True, null=True)  # Field name made lowercase.
    flag_area_u = models.IntegerField(db_column='FLAG_AREA_U', blank=True, null=True)  # Field name made lowercase.
    flag_area_r = models.IntegerField(db_column='FLAG_AREA_R', blank=True, null=True)  # Field name made lowercase.
    cant_viv_marco = models.IntegerField(db_column='CANT_VIV_MARCO', blank=True, null=True)  # Field name made lowercase.
    cant_mzs_marco = models.IntegerField(db_column='CANT_MZS_MARCO', blank=True, null=True)  # Field name made lowercase.
    cant_ccpp_marco = models.IntegerField(db_column='CANT_CCPP_MARCO', blank=True, null=True)  # Field name made lowercase.
    fase = models.CharField(db_column='FASE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    #id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    porcent_segm = models.DecimalField(db_column='PORCENT_SEGM', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    cant_viv_marco_u = models.IntegerField(db_column='CANT_VIV_MARCO_U', blank=True, null=True)  # Field name made lowercase.
    cant_viv_marco_r = models.IntegerField(db_column='CANT_VIV_MARCO_R', blank=True, null=True)  # Field name made lowercase.
    cant_pob_marco_u = models.IntegerField(db_column='CANT_POB_MARCO_U', blank=True, null=True)  # Field name made lowercase.
    cant_pob_marco_r = models.IntegerField(db_column='CANT_POB_MARCO_R', blank=True, null=True)  # Field name made lowercase.
    cant_secc_u = models.IntegerField(db_column='CANT_SECC_U', blank=True, null=True)  # Field name made lowercase.
    cant_ae_u = models.IntegerField(db_column='CANT_AE_U', blank=True, null=True)  # Field name made lowercase.
    cant_secc_r = models.IntegerField(db_column='CANT_SECC_R', blank=True, null=True)  # Field name made lowercase.
    cant_ae_r = models.IntegerField(db_column='CANT_AE_R', blank=True, null=True)  # Field name made lowercase.
    idprovope = models.CharField(db_column='IDPROVOPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cant_subzonas = models.IntegerField(db_column='CANT_SUBZONAS', blank=True, null=True)  # Field name made lowercase.
    porcent_segm_calidad = models.DecimalField(db_column='PORCENT_SEGM_CALIDAD', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    flag_calidad_u = models.IntegerField(db_column='FLAG_CALIDAD_U', blank=True, null=True)  # Field name made lowercase.
    flag_calidad_r = models.IntegerField(db_column='FLAG_CALIDAD_R', blank=True, null=True)  # Field name made lowercase.
    ord_dist_censal = models.IntegerField(db_column='ORD_DIST_CENSAL', blank=True, null=True)  # Field name made lowercase.
    idsubprov_censal = models.CharField(db_column='IDSUBPROV_CENSAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    nombsubprov_censal = models.CharField(db_column='NOMBSUBPROV_CENSAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idprov_censal = models.CharField(db_column='IDPROV_CENSAL', max_length=3, blank=True, null=True)  # Field name made lowercase.
    nombprov_censal = models.CharField(db_column='NOMBPROV_CENSAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idsubdep_censal = models.CharField(db_column='IDSUBDEP_CENSAL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nombsubdep_censal = models.CharField(db_column='NOMBSUBDEP_CENSAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    iddep_censal = models.CharField(db_column='IDDEP_CENSAL', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nombdep_censal = models.CharField(db_column='NOMBDEP_CENSAL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=20, blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='GRUPO', max_length=60, blank=True, null=True)  # Field name made lowercase.
    idregion = models.IntegerField(db_column='IDREGION', blank=True, null=True)  # Field name made lowercase.
    flag_leido_udra = models.IntegerField(db_column='FLAG_LEIDO_UDRA', blank=True, null=True)  # Field name made lowercase.
    flag_cerrado = models.IntegerField(db_column='FLAG_CERRADO', blank=True, null=True)  # Field name made lowercase.
    id_tipo = models.IntegerField(db_column='ID_TIPO', blank=True, null=True)  # Field name made lowercase.
    tipo_distrito = models.CharField(db_column='TIPO_DISTRITO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    idciudad = models.CharField(db_column='IDCIUDAD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    nombciudad = models.CharField(db_column='NOMBCIUDAD', max_length=100, blank=True, null=True)  # Field name made lowercase.
    cant_comunidad = models.IntegerField(db_column='CANT_COMUNIDAD', blank=True, null=True)  # Field name made lowercase.
    pea_coordinador_ci = models.IntegerField(db_column='PEA_COORDINADOR_CI', blank=True, null=True)  # Field name made lowercase.
    pea_jefe_distrital_ci = models.IntegerField(db_column='PEA_JEFE_DISTRITAL_CI', blank=True, null=True)  # Field name made lowercase.
    cant_pea_zona = models.IntegerField(db_column='CANT_PEA_ZONA', blank=True, null=True)  # Field name made lowercase.
    cant_pea_subzona = models.IntegerField(db_column='CANT_PEA_SUBZONA', blank=True, null=True)  # Field name made lowercase.
    cant_pea_secc_u = models.IntegerField(db_column='CANT_PEA_SECC_U', blank=True, null=True)  # Field name made lowercase.
    cant_pea_secc_r = models.IntegerField(db_column='CANT_PEA_SECC_R', blank=True, null=True)  # Field name made lowercase.
    cant_pea_ae_u = models.IntegerField(db_column='CANT_PEA_AE_U', blank=True, null=True)  # Field name made lowercase.
    cant_pea_ae_r = models.IntegerField(db_column='CANT_PEA_AE_R', blank=True, null=True)  # Field name made lowercase.
    flag_imp_emp_especial = models.IntegerField(db_column='FLAG_IMP_EMP_ESPECIAL', blank=True, null=True)  # Field name made lowercase.
    flag_conflicto = models.IntegerField(db_column='FLAG_CONFLICTO', blank=True, null=True)  # Field name made lowercase.
    ubigeo_conflicto = models.CharField(db_column='UBIGEO_CONFLICTO', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = True
        db_table = 'marco_distritos'


class Zona(models.Model):
    #id = models.IntegerField(db_column='ID',primary_key=True)  # Field name made lowercase.
    idzona = models.CharField(db_column='IDZONA', max_length=25, primary_key=True)  # Field name made lowercase.
    ubigeo = models.ForeignKey(Distrito,db_column='UBIGEO',on_delete=False,blank=True,null=True)  # Field name made lowercase.
    region = models.CharField(db_column='REGION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    grupo = models.CharField(db_column='GRUPO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nombdep = models.CharField(db_column='NOMBDEP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nombprov = models.CharField(db_column='NOMBPROV', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nombdist = models.CharField(db_column='NOMBDIST', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zona = models.CharField(db_column='ZONA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    codccpp = models.CharField(db_column='CODCCPP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    nomccpp = models.CharField(db_column='NOMCCPP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ccdd = models.CharField(db_column='CCDD', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ccpp = models.CharField(db_column='CCPP', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ccdi = models.CharField(db_column='CCDI', max_length=2, blank=True, null=True)  # Field name made lowercase.
    etiq_zona = models.CharField(db_column='ETIQ_ZONA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cant_mzs_marco = models.IntegerField(db_column='CANT_MZS_MARCO', blank=True, null=True)  # Field name made lowercase.
    cant_viv_marco = models.IntegerField(db_column='CANT_VIV_MARCO', blank=True, null=True)  # Field name made lowercase.
    cant_pob_marco = models.IntegerField(db_column='CANT_POB_MARCO', blank=True, null=True)  # Field name made lowercase.
    flag_proc_segm = models.IntegerField(db_column='FLAG_PROC_SEGM', blank=True, null=True)  # Field name made lowercase.
    equipo_proc_segm = models.CharField(db_column='EQUIPO_PROC_SEGM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fec_proc_segm = models.DateTimeField(db_column='FEC_PROC_SEGM', blank=True, null=True)  # Field name made lowercase.
    fase = models.CharField(db_column='FASE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    iddistope = models.CharField(db_column='IDDISTOPE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    distope = models.CharField(db_column='DISTOPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    cant_secc_u = models.IntegerField(db_column='CANT_SECC_U', blank=True, null=True)  # Field name made lowercase.
    cant_ae_u = models.IntegerField(db_column='CANT_AE_U', blank=True, null=True)  # Field name made lowercase.
    flag_imp_total = models.IntegerField(db_column='FLAG_IMP_TOTAL', blank=True, null=True)  # Field name made lowercase.
    flag_selec = models.IntegerField(db_column='FLAG_SELEC', blank=True, null=True)  # Field name made lowercase.
    flag_selec_estudiantes = models.IntegerField(db_column='FLAG_SELEC_ESTUDIANTES', blank=True, null=True)  # Field name made lowercase.
    flag_data_insert = models.IntegerField(db_column='FLAG_DATA_INSERT', blank=True, null=True)  # Field name made lowercase.
    flag_reproc = models.IntegerField(db_column='FLAG_REPROC', blank=True, null=True)  # Field name made lowercase.
    n_reproc = models.IntegerField(db_column='N_REPROC', blank=True, null=True)  # Field name made lowercase.

    flag_leido_udra = models.IntegerField(db_column='FLAG_LEIDO_UDRA', blank=True, null=True)  # Field name made lowercase.
    error = models.CharField(db_column='ERROR', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    tiene_tb_mzs = models.CharField(db_column='TIENE_TB_MZS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tiene_tb_viv_consistencia = models.CharField(db_column='TIENE_TB_VIV_CONSISTENCIA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tiene_tb_viv_cartografia = models.CharField(db_column='TIENE_TB_VIV_CARTOGRAFIA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tiene_tb_puntos_inicio = models.CharField(db_column='TIENE_TB_PUNTOS_INICIO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tiene_tb_frentes = models.CharField(db_column='TIENE_TB_FRENTES', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tiene_tb_ejes_viales = models.CharField(db_column='TIENE_TB_EJES_VIALES', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tiene_tb_sitio_interes = models.CharField(db_column='TIENE_TB_SITIO_INTERES', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tiene_tb_pseudocodigo = models.CharField(db_column='TIENE_TB_PSEUDOCODIGO', max_length=5, blank=True, null=True)  # Field name made lowercase.
    flag_exist_capas = models.CharField(db_column='FLAG_EXIST_CAPAS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    tiene_tb_zona = models.CharField(db_column='TIENE_TB_ZONA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cant_subzonas = models.IntegerField(db_column='CANT_SUBZONAS', blank=True, null=True)  # Field name made lowercase.
    nombdistope = models.CharField(db_column='NOMBDISTOPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ubigeo_conflicto = models.CharField(db_column='UBIGEO_CONFLICTO', max_length=6, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed = True
        db_table = 'marco_zonas'
