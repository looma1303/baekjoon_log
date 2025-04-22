dots = list()
for x in range(0,3):
    n = input()
    n = n.split()
    dots.append([int(n[0]), int(n[1])])
    
x_position = list()
y_position = list()
for x in dots:
    x_position.append(x[0])
    y_position.append(x[1])

answer = list()
if x_position[0] == x_position[1]:
    answer.append(x_position[2])
elif x_position[1] == x_position[2]:
    answer.append(x_position[0])
elif x_position[0] == x_position[2]:
    answer.append(x_position[1])
else:
    pass

if y_position[0] == y_position[1]:
    answer.append(y_position[2])
elif y_position[1] == y_position[2]:
    answer.append(y_position[0])
elif y_position[0] == y_position[2]:
    answer.append(y_position[1])
else:
    pass

print(str(answer[0]) + ' ' + str(answer[1]))


    
    