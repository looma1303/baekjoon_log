subject_count = int(input())
#과목 개수를 받는다
subject_score = input()
#str형태로 점수를 받는다

subject_score = subject_score.split()
for x in range(0, subject_count):
    subject_score[x] = int(subject_score[x])    
#str -> list

subject_score.sort()
highest = subject_score[subject_count-1]
#가장 높은 점수 찾기

for x in range(0, subject_count):
    subject_score[x] = subject_score[x] / highest * 100
#과목점수를 점수/highest * 100 으로 고치기




y = 0
for x in subject_score:
    y = y+x
    
#과목 점수 다 합하기

score_average = y / subject_count
print(score_average)