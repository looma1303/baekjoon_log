n = input()
a = list()
b = list()
n = n.split(' ')
result = list()
for x in range(0, 2):
    n[x] = int(n[x])

for x in range(0, n[0]):
    q = input()
    q = q.split(' ')
    for y in range(0, n[1]):
        q[y] = int(q[y])
    a.append(q)

for x in range(0, n[0]):
    q = input()
    q = q.split(' ')
    for y in range(0, n[1]):
        q[y] = int(q[y])
    b.append(q)

for x in range(0, n[0]):
    result.append([])
for x in range(0, n[0]):
    for y in range(0, n[1]):
        result[x].append(a[x][y] + b[x][y])

for x in range(0, n[0]):
    for y in range(0, n[1]):
        print(result[x][y], end=' ')

    print('')






