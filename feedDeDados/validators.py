from django.core.exceptions import ValidationError

def validaArquivo(value):
    try:
        open('static/datasets/'+value, newline="")
    except IOError:
        raise ValidationError(
            (value+" não existe no diretório 'datasets'"),
            params={'value': value},
        )