entrada = input().split()
tempos = []
for i in range(len(entrada)):
    tempos.append(int(entrada[i]))
if len(set(tempos)) == 1:
    saida = "O JOGO DUROU %3i HORA(S) E %3i MINUTO(S)" % (24,0)
else:
    if tempos[0] < tempos[2]:
        horas = tempos[2]-tempos[0]
    else:
        horas = (24-tempos[0])+tempos[2]
    if tempos[1] > tempos[3]:
        minutos = 60 - (tempos[1] - tempos[3])
        horas -= 1
    else:
        minutos = tempos[3] - tempos[1]
    saida = "O JOGO DUROU %3i HORA(S) E %3i MINUTO(S)" % (horas, minutos)
print(saida)