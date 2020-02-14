from django.db import models
# Feel free to rename the models, but don't rename db_table values or field names.



class Pru(models.Model):
    id_t = models.IntegerField(primary_key=True)
    descripcion_t = models.CharField(max_length=50, blank=True, null=True)
    id_foraneo_t = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pru'


class Pru2(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    id_foraneo = models.ForeignKey(Pru, models.DO_NOTHING, db_column='id_foraneo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pru2'