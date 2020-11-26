import csv
with open('datasets/notas.csv', newline="") as entradaCsv:
    leitorCsv = csv.DictReader(entradaCsv)
    dicionarioDeCr = {}
    for linha in leitorCsv:
        if dicionarioDeCr.get(linha['MATRICULA'], None) != None:
            dicionarioDeCr[linha['MATRICULA']] = [int(linha["NOTA"]) + int(dicionarioDeCr[linha['MATRICULA']][0]), dicionarioDeCr[linha['MATRICULA']][1] + 1]
        else:
            dicionarioDeCr[linha['MATRICULA']] = [int(linha["NOTA"]), 1]
    print(dicionarioDeCr)