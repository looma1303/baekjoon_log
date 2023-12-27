n = int(input())
result = list()
q = list()
for x in range(0, n):
    s = input()
    for y in s:
        while y + y in s:
            s = s.replace(y + y, y)
    q.append(s)

for x in q:
    check_list = list()
    for y in range(0, len(x)):
        if x[y] in check_list:
            check_list.append(0)
            break
        else:
            check_list.append(x[y])

    if 0 in check_list:
        result.append(0)
    else:
        result.append(1)

i = 0
for x in result:
    if x == 0:
        pass
    else:
        i = i + 1

print(i)







