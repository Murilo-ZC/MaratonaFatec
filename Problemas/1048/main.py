salario_base = float(input())

if salario_base <= 400:
    aumento = 0.15
elif salario_base <= 800:
    aumento = 0.12
elif salario_base <= 1200:
    aumento = 0.10
elif salario_base <= 2000:
    aumento = 0.07
else:
    aumento = 0.04
reajuste = aumento * salario_base
novo_salario = reajuste + salario_base
print("Novo salario: %.2f" % novo_salario)
print("Reajuste ganho: %.2f" % reajuste)
print("Em percentual: %.0f %s" % (aumento*100, '%'))