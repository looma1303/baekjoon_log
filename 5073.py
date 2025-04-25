data = list()
while True:
    q = list()
    n = input()
    n = n.split()
    for x in n:
        q.append(int(x))
        
    if q == [0, 0, 0]:
        break 
    else:
        data.append(q)
        
for x in data:
    x.sort()
    first = x[0]
    sec = x[1]
    trd = x[2]
    if trd >= first + sec:
        print("Invalid")
    elif first == sec and sec == trd:
        print('Equilateral')
    elif first == sec or sec == trd or first == trd:
        print('Isosceles')
    else:
        print('Scalene')
    