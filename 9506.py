data = list()
while True:
    n = input()
    if n == '-1':
        break
    else:
        data.append(int(n))
        

for x in data:
    num = []
    for y in range(1,x+1):
        if x % y == 0:
            num.append(y)
        else:
            pass
    
    del num[len(num) - 1]
    if sum(num) == x:
        #str을 만들어야함.
        result = str(x) + ' ' + '=' + ' '
        q = 0
        for z in num:
            q += 1
            if q < len(num): 
                result += str(z) + ' ' + '+' + ' '
            else:
                result += str(z)
            
            
        print(result)
    else:
        print(str(x) + ' ' + 'is NOT perfect.')