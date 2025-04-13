for x in range(0,2):
    if x == 0:
        first = input()
        first = int(first)
    else:
        second = input()
        second = int(second)
        
    
num = list()
for x in range(first, second + 1):
    if x > 10:
        if x % 2 == 0 or x % 3 == 0 or x % 5 == 0 or x % 7 == 0:
            pass
        elif (x ** (1/2)) == int((x ** (1/2))): 
            pass
        else:
            q = 0
            for y in range(2, x + 1):
                if x % y == 0:
                    q += 1
                else:
                    pass
                
                if q > 1:
                    break
            if q == 1:
                num.append(x)
            else: pass 
    else:
        q = 0
        for y in range(2, x + 1):
            if x % y == 0:
                q += 1
            else:
                pass
                
            if q > 1:
                break
        if q == 1:
            num.append(x)
        else: pass 
        

if len(num) == 0:
    print(-1)
else:
    print(sum(num))
    print(num[0])