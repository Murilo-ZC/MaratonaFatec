# -*- coding: utf-8 -*-
C = int(input())

for i in range(C):
    entrada = input()
    nome, forca = entrada.split()
    if nome.upper() == "THOR":
        print('Y')
    else:
        print('N')


