


def d(n):
    #문제에서 나온 d를 구현하기
    num_split = list()
    for x in str(n):
        num_split.append(x)
        
        
    sum_num = n
    for x in num_split:
        sum_num = sum_num + int(x)
        
    result = sum_num
    
    return result
    num_split.clear()


not_self_num = list()



for x in range(1,10001):
    n = d(x)
    if n not in not_self_num:
        not_self_num.append(n)
    else:
        pass
    

for x in range(1,10001):
    if x in not_self_num:
        pass
    else:
        print(x)
        