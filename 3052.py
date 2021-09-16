a = list()
b = list()
c = list()
for x in range(0,10):
    a.append(int(input()))
    
    
for y in a:
    b = y % 42
    if b not in c:
        c.append(b)
        
print(len(c))
        
    
    
    
    