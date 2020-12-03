from django.db import models
import csv
from aluno.models import Aluno, DisciplinaCursada
from disciplina.models import Disciplina
from curso.models import Curso
from feedDeDados.validators import validaArquivo, validaNomeArquivo
from django.core.validators import RegexValidator
import time



class FeedDeDados(models.Model):
    nomeArquivo = models.CharField(max_length=100, db_index=True, unique=True, validators=[
            RegexValidator(regex='^[a-z0-9A-Z]+\.csv$', message='O arquivo de dados precisa ser do formato CSV.'), validaNomeArquivo])
    dataCarregamento = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'feedDeDados'
        get_latest_by = 'dataCarregamento'

    def __str__(self):
        return self.nomeArquivo

    def populaBd(self):
        start_time = time.time()
        with open('static/datasets/'+self.nomeArquivo, newline="") as entradaCsv:
            leitorCsv = csv.DictReader(entradaCsv)
            for linha in leitorCsv:
                aluno = Aluno(matricula=linha["MATRICULA"])
                curso = Curso(codigo=linha["COD_CURSO"])
                disciplina = Disciplina(codigo=linha["COD_DISCIPLINA"], cargaHoraria=linha["CARGA_HORARIA"],cursoAssociado=curso)
                disciplinaCursada = DisciplinaCursada(disciplina=disciplina, aluno=aluno, nota=linha["NOTA"], anoSemestre=linha["ANO_SEMESTRE"])
                aluno.save()
                curso.save()
                disciplina.save()
                disciplinaCursada.save()
        print("--- %s sem Bulk ---" % (time.time() - start_time))
            
    def populaBdBulk(self):
        start_time = time.time()
        with open('static/datasets/'+self.nomeArquivo, newline="") as entradaCsv:
            leitorCsv = csv.DictReader(entradaCsv)
            lAluno = {}
            lCurso = {}
            lDisciplina = {}
            lDisciplinaCursada = []
            for linha in leitorCsv:
                aluno = Aluno(matricula=linha["MATRICULA"])
                curso = Curso(codigo=linha["COD_CURSO"])
                disciplina = Disciplina(codigo=linha["COD_DISCIPLINA"], cargaHoraria=linha["CARGA_HORARIA"],cursoAssociado=curso)
                disciplinaCursada = DisciplinaCursada(disciplina=disciplina, aluno=aluno, nota=linha["NOTA"], anoSemestre=linha["ANO_SEMESTRE"])
                lAluno[aluno] = None
                lCurso[curso] = None
                lDisciplina[disciplina] = None
                lDisciplinaCursada.append(disciplinaCursada)
            lAluno = list(lAluno)
            lCurso = list(lCurso)
            lDisciplina = list(lDisciplina)
            Aluno.objects.bulk_create(lAluno)
            Curso.objects.bulk_create(lCurso)
            Disciplina.objects.bulk_create(lDisciplina)
            DisciplinaCursada.objects.bulk_create(lDisciplinaCursada)
        print("--- %s com Bulk ---" % (time.time() - start_time))

    def apagaBd(self):
        DisciplinaCursada.objects.all().delete()
        Disciplina.objects.all().delete()
        Aluno.objects.all().delete()
        Curso.objects.all().delete()
    
    def substituiBd(self):
        self.apagaBd()
        self.populaBdBulk()