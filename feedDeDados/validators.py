from django.core.exceptions import ValidationError

def validaArquivo(value):
    try:
        open('static/datasets/'+value.nomeArquivo, newline="")
    except IOError:
        raise ValidationError(
            ("O arquivo '"+value.nomeArquivo+"' não existe no diretório datasets"),
            params={'value': value},
        )

def validaNomeArquivo(value):
    try:
        open('static/datasets/'+value, newline="")
    except IOError:
        raise ValidationError(
            ("O arquivo '"+value+"' não existe no diretório datasets"),
            params={'value': value},
        )