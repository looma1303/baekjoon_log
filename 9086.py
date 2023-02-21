n = input()
str_list = list()
for x in range(0, int(n)):
    q = input()
    str_list.append(q)

for x in str_list:
    if len(x) == 1:
        print(x+x)
    else:
        print(x[0]+x[len(x)-1])
    