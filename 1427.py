n = input()
data = list()
for x in n:
    data.append(int(x))

data.sort(reverse=True)

for x in data:
    print(x, end="")