n = input()
data = input()

n = n.split()
data = data.split()

for x in range(0,len(n)):
    n[x] = int(n[x])
    
for x in range(0,len(data)):
    data[x] = int(data[x])
    
    
big_number = list()
num = n[1]
card = data
between = list()

for x in card:
    q = sorted(card)
    q.remove(x)
    for y in q:
        t = sorted(q)
        t = t.remove(y)
        for z in t:
            big_number.append(x + y + z)
            
            
big_number.sort()
a = sorted(big_number)
for x in a:
    if x > num:
        big_number.remove(x)
    


big_number.sort(reverse=True)


            

print(big_number[0])
                
        

