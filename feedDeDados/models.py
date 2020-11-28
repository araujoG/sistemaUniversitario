from django.db import models
import csv
from aluno.models import Aluno, DisciplinaCursada
from disciplina.models import Disciplina

class FeedDeDados(models.Model):
    nomeArquivo = models.CharField(max_length=100, db_index=True, unique=True)
    dataCarregamento = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'feedDeDados'
        get_latest_by = 'dataCarregamento'

    def __str__(self):
        return self.nomeArquivo

    def populaBd(self):
        with open('static/datasets/'+self.nomeArquivo, newline="") as entradaCsv:
            leitorCsv = csv.DictReader(entradaCsv)
            for linha in leitorCsv:
                aluno = Aluno(matricula=linha["MATRICULA"],curso = linha["COD_CURSO"])
                disciplina = Disciplina(codigo=linha["COD_DISCIPLINA"], cargaHoraria=linha["CARGA_HORARIA"])
                disciplinaCursada = DisciplinaCursada(disciplina=disciplina, aluno=aluno, nota=linha["NOTA"], anoSemestre=linha["ANO_SEMESTRE"])
                print(aluno)
                aluno.save()
                disciplina.save()
                disciplinaCursada.save()
                break;

    def apagaBd(self):
        DisciplinaCursada.objects.all().delete()
        Disciplina.objects.all().delete()
        Aluno.objects.all().delete()
    
    def substituiBd(self):
        self.apagaBd()
        self.populaBd()
    