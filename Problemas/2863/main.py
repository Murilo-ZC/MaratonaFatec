while True:
    try:
        N = int(input())
        tempos = []
        for i in range(N):
            tempos.append(float(input()))
        tempo = min(tempos)
        print(tempo)
    except:
        break