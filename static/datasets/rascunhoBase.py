import csv
# with open('static/datasets/notas.csv', newline="") as entradaCsv:
#     leitorCsv = csv.DictReader(entradaCsv)
#     dicionarioDeCr = {}
#     for linha in leitorCsv:
#         if dicionarioDeCr.get(linha['MATRICULA'], None) != None:
#             dicionarioDeCr[linha['MATRICULA']] = [int(linha["NOTA"]) + int(dicionarioDeCr[linha['MATRICULA']][0]), dicionarioDeCr[linha['MATRICULA']][1] + 1]
#         else:
#             dicionarioDeCr[linha['MATRICULA']] = [int(linha["NOTA"]), 1]
#     print(dicionarioDeCr)


try:
    open('static/datasets/a', newline="")
except IOError:
    print ("Error: File does not appear to exist.")
