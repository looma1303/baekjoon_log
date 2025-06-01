q = input()
q = q.split()
data = list()
for x in q:
    data.append(int(x))
    
c = int(input())
n0 = int(input())
a1 = data[0]
a0 = data[1]



if a1*n0 + a0 <= c*n0 and a1 <= c:
    print(1)
else:
    print(0)
        


    

    
    