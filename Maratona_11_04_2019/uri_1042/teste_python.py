# -*- coding: utf-8 -*-
linha = input()
numeros = linha.split(' ')

for i in range(3):
    numeros[i] = int(numeros[i])
    
lista_para_ordenar = numeros.copy()
lista_para_ordenar.sort()

for item in lista_para_ordenar:
    print(item)

print()

for item in numeros:
    print(item)

