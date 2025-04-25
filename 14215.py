n = input()
n = n.split()
data = list()
for x in n:
    data.append(int(x))

data.sort()

while True:
    if data[2] < data[0] + data[1]:
        break
    else:
        data[2] -= 1

        
        
print(sum(data))