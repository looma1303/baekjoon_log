total = int(input())
num = int(input())
result = 0
a = list()

for x in range(0,num):
    n = input()
    n = n.split()
    for y in n:
        a.append(int(y))
    result = result + (a[0] * a[1])
    a = []
    



if result == total:
    print('Yes')    
else:
    print('No')