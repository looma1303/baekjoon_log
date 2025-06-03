#입력 받기
n = input()
n = n.split()
result = list()
for x in range(0,2):
    if x == 0:
        M = int(n[0])
    else:
        N = int(n[1])
        
paper = list()
for x in range(0,M):
    q = input()
    paper.append(q)

#왼쪽 위 칸이 하얀색인 판과, 검은색인 판 생성

white = 'WBWBWBWB'
black = 'BWBWBWBW'
white_pan = list()
black_pan = list()
for x in range(0,8):
    if x % 2 == 0:
        white_pan.append(white)
        black_pan.append(black)
    else:
        white_pan.append(black)
        black_pan.append(white)
        
#입력받은 종이를 8,8으로 슬라이스 할 수 있는 모든 경우의 수 구하기. 
M_time = M - 7
N_time = N - 7

total_time = M_time + N_time

#입력받은값 슬라이싱하기.

for x in range(0,M_time):
    M_start = x
    M_end = x + 7
    #x번째 줄 부터, x+7번째 줄까지 가져오기.
    M_pan = paper.copy()
    M_pan = M_pan[M_start:M_end+1]
    for y in range(0, N_time):
        N_pan = []
        N_start = y 
        N_end = y + 7
        for z in M_pan:
            N_pan.append(z[N_start:N_end+1])
        
        #White_pan,black_pan과 N_이랑 비교해서 값이 다른 값의 수가 더 작은 값 저장하기.
        
        uw = 0
        ub = 0
        for q in range(0,8):
            for t in range(0,8):
                if white_pan[q][t] != N_pan[q][t]:
                    
                    uw += 1
                elif black_pan[q][t] != N_pan[q][t]:
                    
                    ub += 1
                else:
                    pass
                    
                    
        
        if uw <= ub:
            result.append(uw)
        else:
            result.append(ub)
        
                    
#저장된 값 정렬해서 가장 작은 값 리턴하기.          
result.sort()
print(result[0])           
        


    
    