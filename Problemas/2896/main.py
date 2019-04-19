N = int(input())

for i in range(N):
    n1 , n2 = input().split()
    n1 = int(n1)
    n2 = int(n2)
    print((n1//n2 + n1 % n2)) 