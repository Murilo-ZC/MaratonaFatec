word1 = input()
word2 = input()
word3 = input()

if word1 == 'vertebrado':
    if word2 == 'ave':
        if word3 == 'carnivoro':
            saida = 'aguia'
        elif word3 == 'onivoro':
            saida = 'pomba'
    elif word2 == 'mamifero':
        if word3 == 'herbivoro':
            saida = 'vaca'
        elif word3 == 'onivoro':
            saida = 'homem'
elif word1 == 'invertebrado':
    if word2 == 'inseto':
        if word3 == 'hematofago':
            saida = 'pulga'
        elif word3 == 'herbivoro':
            saida = 'lagarta'
    elif word2 == 'anelideo':
        if word3 == 'hematofago':
            saida = 'sanguessuga'
        elif word3 == 'onivoro':
            saida = 'minhoca'
else:
    saida = 'Nao classificado'
print(saida)    