#data 받기
n = input()
data = input()

n = n.split()
data = data.split()

for x in range(0,len(n)):
    n[x] = int(n[x])
    
for x in range(0,len(data)):
    data[x] = int(data[x])

    
#data -> card(dict) 형태로 저장
card = dict()
for x in range(0, len(data)):
    card[x] = data[x]
    
sum_list = list() #카드의 합을 저장할 list 생성
    
    
#다른 카드 끼리만 더할 수 있도록 설계
for x in range(0, len(card)):
    for y in range(0, len(card)):
        for z in range(0, len(card)):
            if x == y or x == z or y == z:
                pass
            else:
                sum_list.append(card[x]+card[y]+card[z])
                
number = n[1] #가까워야 하는 숫자 변수 지정

#정렬된 sum_list 생성

sorted_sum_list = sorted(sum_list)

#정렬된 sum_list의 숫자중 number보다 큰 숫자의 가장 처음 위치 찾기.

for x in range(0, len(sorted_sum_list)):
    if sorted_sum_list[x] > number:
        first_big_sum_point = x
        break
    else:
        #만약 없다면 가장 큰 수를 sorted_sum_list의 len으로 지정하기
        first_big_sum_point = len(sorted_sum_list)
    
#정렬된 sum_list의 number보다 큰 숫자 뒤에 있는 숫자들은 삭제.

sorted_sum_list = sorted_sum_list[0:first_big_sum_point-1]

#sorted_sum_list의 가장 뒤에 있는 숫자 print
print(sorted_sum_list[len(sorted_sum_list)-1])
                
    