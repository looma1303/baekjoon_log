data = list()
result = 0.0
subject_score = 0.0
for x in range(0,20):
    n = input()
    n = n.split(' ')
    del n[0]
    if n[1] == 'A+':
        score = 4.5
    elif n[1] == 'A0':
        score = 4.0
    elif n[1] == 'B+':
        score = 3.5
    elif n[1] == 'B0':
        score = 3.0
    elif n[1] == 'C+':
        score = 2.5
    elif n[1] == 'C0':
        score = 2.0
    elif n[1] == 'D+':
        score = 1.5
    elif n[1] == 'D0':
        score = 1.0
    elif n[1] == 'P':
        n[0] = 0.0
        score = 0.0
    else:
        score = 0.0

    result = result + (score * float(n[0]))
    subject_score = subject_score + float(n[0])

print(result/subject_score)




