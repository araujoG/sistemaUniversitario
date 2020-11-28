from django.db import models

class Curso (models.Model):
    codigo = models.CharField(max_length=8, db_index=True, unique=True, primary_key=True)

    class Meta:
        db_table = 'curso'

    def __str__(self):
        return self.codigo

