n = int(input())

case_list = list()
to_int = list()
result = list()

for x in range(0,n):
    test_case = input()
    test_case = test_case.split()
    for y in test_case:
        to_int.append(int(y))
        
    case_list.append(to_int)
    to_int = []
    
for x in case_list:
    stu_num = x[0]
    del x[0]
    total_score = 0
    for y in x:
        total_score = total_score + y
    
    average = total_score / stu_num
    high_stu_count = 0
    for z in x:
        if z > average:
            high_stu_count = high_stu_count + 1
            
        else:
            pass
    
    a = (high_stu_count / stu_num * 100 )
    result.append('{:.3f}'.format(round(a,3)))
    
for x in result:
    print(x+'%')
   
        
    
    

    

    
    
