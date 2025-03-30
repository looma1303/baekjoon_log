case = list()
result = list()
while True:
    n = input()
    n = n.split()
    n[0] = int(n[0])
    n[1] = int(n[1])
    
    if n[0] == 0 and n[1] == 0:
        break 
        
    else:
        case.append(n)
        
for x in case:
    if x[0] < x[1]:
        if x[1] % x[0] == 0:
            result.append('factor')
        else:
            result.append('neither')
    else:
        if x[0] % x[1] ==0:
            result.append('multiple')
        else:
            result.append('neither')
            
for x in result:
    print(x)
            
