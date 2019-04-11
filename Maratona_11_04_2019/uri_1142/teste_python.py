# -*- coding: utf-8 -*-
N = int(input())
conta = 0

for i in range(N):
    for j in range(4):
        conta = conta + 1
        if conta % 4 == 0:
            print("PUM", end = '\n')
            break
        else:    
            print(conta, end=' ')
        


