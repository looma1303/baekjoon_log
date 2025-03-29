n = input()
n = int(n)

if n == 1:
    print('1/1')
else: #극단 범위, 극단 수 찾기.
    point = [1,1]
    num = 1
    end = 1
    while True:
        if end >= n:
            num -= 1
            break
        else:
            num += 1
            end = end + num

            


    #end: 극단 범위, num: 극단 수    
    start = end - num
    num += 1
    if num % 2 == 0:
        point = [1 , num]
        way = 'd'
    else:
        point = [num, 1]
        way = 'u'
        
        
    if n == start:
        print(str(point[0])+'/'+str(point[1]))
    else:
        while True:
            if n == start:
                break
                
            else:
                start += 1
                if way == 'd':
                    point[0] += 1
                    point[1] -= 1
                else:
                    point[0] -= 1
                    point[1] += 1
        print(str(point[0])+'/'+str(point[1]))
                    
                    

