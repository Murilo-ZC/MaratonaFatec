d1,d2 = input().split()
d1 = int(d1)
d2 = int(d2)

if (d2 - d1) >= 3:
    print("Muito bem! Apresenta antes do Natal!")
else:
    print("Parece o trabalho do meu filho!")
    if (d1 + 2) >= 24:
        print("Fail! Entao eh nataaaaal!")
    else:
        print("TCC Apresentado!")