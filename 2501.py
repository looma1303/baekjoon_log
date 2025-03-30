n = input()
n = n.split()
n[0] = int(n[0])
n[1] = int(n[1])

N = n[0]
K = n[1]
result = list()

for x in range(1, N+1):
    if N % x == 0:
        result.append(x)
    else:
        pass
try:
    print(result[K-1])
except:
    print(0)