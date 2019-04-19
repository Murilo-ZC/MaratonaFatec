entrada = input().split()
lados = []
for i in range(len(entrada)):
    lados.append(float(entrada[i]))
A,B,C = sorted(lados, reverse=True)
if A >= (B+C):
    saida = "Area = %.1f" % ((lados[0] + lados[1])*lados[2]/2)
else:
    saida = "Perimetro = %.1f" % (sum(lados))
print(saida)