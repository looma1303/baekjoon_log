n = input()
k = list()
for a in n:
    k.append(a)

for x in range(0, len(k)):
    if k[x] == k[len(k)-1-x]:
        result = 1
        
    else:
        result = 0
        break
    
print(result)
        
