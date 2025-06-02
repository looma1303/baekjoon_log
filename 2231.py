#숫자 받기
n = int(input())
#정답의 초기값을 0으로 한다.
result = 0
#분해합 찾기
#1부터 n까지 for문을 돌려서 x와 x를 이루는 자리수의 합이 n이 되는것을 찾는다.

for x in range(1,n+1):
    #x의 자리수가 1이면 pass한다.
    
    q = list() #각 자리수의 값을 저장할 list를 생성한다.
    for y in str(x):
        q.append(int(y))
    if x + sum(q) == n:#만약 x + 각 자리 수의 합이 n이라면
        result = x
        break
    else:
        pass
        
print(result)
            
            