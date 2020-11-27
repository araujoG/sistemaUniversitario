from django.db import models

class Disciplina (models.Model):
    codigo = models.CharField(max_length=8, db_index=True, unique=True, primary_key=True)
    cargaHoraria = models.IntegerField(default=0)


    class Meta:
        db_table = 'disciplina'

    def __str__(self):
        return self.codigo

