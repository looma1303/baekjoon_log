

atd_stu = list()
result = list()


for x in range(1,29):
    n = int(input())
    atd_stu.append(n)
    
    
for x in range(1,31):
    if x not in atd_stu:
        result.append(x)
        
        
result.sort()
print(result[0])
print(result[1])    
 
    
 
        
