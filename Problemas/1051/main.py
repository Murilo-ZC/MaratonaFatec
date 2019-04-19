valor = float(input())
if valor <= 2000:
    saida = 'Isento'
elif valor <= 3000:
    total = (valor-2000) * 0.08
    saida = "R$ %.2f" % total
elif valor <= 4500:
    total = (valor-3000) * 0.18 + 1000 * 0.08
    saida = "R$ %.2f" % total
else:
    total = (valor-4500) * 0.28 + 1500 * 0.18 + 1000 * 0.08
    saida = "R$ %.2f" % total
print(saida)