n = input()
q = list()
s = list()
t = list()
n = n.lower()
for x in n:
    if x not in q:
        q.append(x)
    else:
        pass



for x in q:
    s.append(n.count(x))
  

    

t = sorted(s,reverse=True)
pos = s.index(t[0])

if s.count(t[0]) < 2:
    print(q[pos].upper())
else:
    print("?")
    
    
    