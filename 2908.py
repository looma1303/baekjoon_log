a = input()
a = a.split()
for x in range(0,2):
    a[x] = a[x][::-1]
    a[x] = int(a[x])
    
if a[0] > a[1]:
    print(a[0])
else:
    print(a[1])
    