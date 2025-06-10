import sys
input = sys.stdin.readline
n = int(input())
count = [0] * (10001)  
for _ in range(n):
    num = int(input())
    count[num] += 1 #이떄 오름차순으로 이미 정렬됨
for i in range(1, 10001):
    for _ in range(count[i]): #숫자가 저장되어있는 개수만큼 반복해서 출력
        print(i)
