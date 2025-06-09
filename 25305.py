n = input()
n = n.split()
k = n[1]
q = input()
q = q.split()
for x in range(0,int(n[0])):
    q[x] = int(q[x])
    
q.sort(reverse=True)
print(q[int(k)-1])


    
    