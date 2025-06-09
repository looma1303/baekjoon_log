n = int(input())
data = list()
for x in range(0,n):
    q = int(input())
    data.append(q)

for x in sorted(data):
    print(x)