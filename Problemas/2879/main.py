import math
N = int(input())
uns = 0
for i in range(N):
    uns += 1 if input() == '1' else 0
    
print(N - uns)