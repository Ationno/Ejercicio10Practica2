import re

with open("nombres_1.txt", 'r', encoding='utf-8',) as nombres, open("eval1.txt", 'r') as notas1, open("eval2.txt", 'r') as notas2:
    l_nombres = re.sub("[,' ]", '', nombres.read()).split('\n')
    l_notas1 = re.sub('[\n ]', '', notas1.read()).split(',')
    l_notas2 = re.sub('[\n ]', '', notas2.read()).split(',')
lista_notas = list(map(lambda x, y: int(x) + int(y), l_notas1, l_notas2))
lista_informacion = list(map(lambda x, y: [x, y], l_nombres, lista_notas))

prom = sum(lista_notas)/len(lista_notas)
for elem in lista_informacion:
    if elem[1] < prom:
        print(f'El alumno {elem[0]} tiene una nota menor al promedio')
