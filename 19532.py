n = input()
n = n.split()
#q에 data를 받는다.
q = list()
for x in n:
    q.append(int(x)) 

    
#abcdef를 지정한다. 
a = q[0]
b = q[1]
c = q[2]
d = q[3]
e = q[4]
f = q[5]


#-999~1000의 숫자를 x,y에 for문을 돌려서 만족하는 숫자를 찾는다.
for x in range(-999,1000):
    for y in range(-999,1000):
        if a*x + b*y == c and d*x + e*y == f:
            result = [x,y]
            break 
        else:
            pass
            
print(result[0],result[1])
    