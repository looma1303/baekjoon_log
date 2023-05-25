a = list()
b = list()
T = int(input())
for x in range(0,T):
    n = input()
    n = n.split()
    a.append([int(n[0]), n[1]])
    

for x,y in a:
    var = ""
    for i in range(0,len(y)):
        var = var + y[i]*x
        
    b.append(var)
        

        
for x in b:
    print(x)