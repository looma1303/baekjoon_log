data = list()
for x in range(0,3):
    n = input()
    n = int(n)
    data.append(n)
    
first = data[0]
sec = data[1]
trd = data[2]

if first + sec + trd != 180:
    print('Error')
elif first == sec and sec == trd:
    print('Equilateral')
elif first == sec or sec == trd or first == trd:
    print('Isosceles')
else:
    print('Scalene')