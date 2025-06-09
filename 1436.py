#입력받기
d = int(input())
#숫자 666이 들어간 n번째 큰 수를 찾을때까지 while문 돌리기

n = 0
a = 0
while True:
    a = a+1
    if len(str(a)) < 3 or '666' not in str(a):
        pass
    else:
        n = n +1
        
    if n == d:
        print(a)
        break
    else:
        pass
    
    
    
    


