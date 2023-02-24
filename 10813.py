n = input()
n = n.split()
buk = list()
for x in range(1,int(n[0])+1):
    buk.append(x)
    
for x in range(0,int(n[1])):
    a = input()
    a = a.split()
    container = buk[int(a[0])-1]
    buk[int(a[0])-1] = buk[int(a[1])-1]
    buk[int(a[1])-1] = container
    #print(buk)
    
    
for x in range(0,int(n[0])):
    buk[x] = str(buk[x])
    
result = ' '.join(buk)
print(result)