q = input()
q = q.split()
data = list()
for x in q:
    data.append(int(x))
    
c = int(input())

n0 = int(input())

left_side = data[0] - c

if left_side <= 0:
    left_side = left_side-(left_side)*2
else:
    pass


right_side = data[1]

x = right_side / left_side

if n0 >= x:
    print(1)
else:
    print(0)



    

    
    