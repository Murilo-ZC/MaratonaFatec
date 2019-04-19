"""

    se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
    se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
    se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
    se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
    se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
    se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

"""

entrada = input().split()
lados = []
for i in range(len(entrada)):
    lados.append(float(entrada[i]))

lados.sort(reverse=True)
A,B,C = lados
if A >= (B+C):
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == (B**2 + C**2):
        print("TRIANGULO RETANGULO")
    if A**2 > (B**2 + C**2):
        print("TRIANGULO OBTUSANGULO")
    if A**2 < (B**2 + C**2):
        print("TRIANGULO ACUTANGULO")
    if len(set(lados)) == 1:
        print("TRIANGULO EQUILATERO")
    if len(set(lados)) == 2:
        print("TRIANGULO ISOSCELES")
