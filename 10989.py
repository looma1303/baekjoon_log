import sys
input = sys.stdin.readline
n = int(input())
data = list()
for x in range(0,n):
    q = int(input())
    data.append(q)

data.sort()
for x in data:
    print(x)