entrada = input().split()
tempos = []
for i in range(len(entrada)):
    tempos.append(int(entrada[i]))
if len(set(tempos)) == 1:
    saida = "O JOGO DUROU 24 HORA(S)"
elif tempos[0] < tempos[1]:
    saida = "O JOGO DUROU %i HORA(S)" % (tempos[1]-tempos[0])
else:
    saida = "O JOGO DUROU %i HORA(S)" % ((24-tempos[0])+tempos[1])
print(saida)