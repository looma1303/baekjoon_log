quiz_result_count = int(input())
quiz_result = list()
for x in range(0,quiz_result_count):
    quiz_result.append(input())
quiz_score = list()
for x in range(0,quiz_result_count):
    score = 0
    continue_count = 0
    for y in quiz_result[x]:
        if y == 'O':
            score = score + 1 + continue_count
            continue_count = continue_count + 1
        else:
            continue_count = 0
    quiz_score.append(score)
for x in quiz_score:
    print(x)
