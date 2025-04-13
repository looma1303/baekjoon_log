data = list()
for x in range(0,2):
    n = input()
    if x == 0:
        pass
    else:
        
        n = n.split()
        for y in n:
            data.append(int(y))
            
            
d = 0   
for x in data:
    q = 0
    for y in range(1,x+1):
        if x % y == 0:
            q += 1
        else:
            pass
    if q == 2:
        d += 1
    else:
        pass
    
print(d)
        
        