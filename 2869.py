import math
n = input()
n = n.split()

n_list = list()
for x in range(0,3):
    n_list.append(int(n[x]))
    

A = n_list[0]
B = n_list[1]
V = n_list[2]
Q = 0

day = (V-A) / (A-B)#전날까지 거리

day = math.ceil(day)

day += 1


print(day)
    
    
        
        

        
    