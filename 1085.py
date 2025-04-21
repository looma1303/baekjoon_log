n = input()
n = n.split(' ')
data = []
for x in n:
    data.append(float(x))
    
hansu = [data[0],data[1]]

right_up = [data[2], data[3]]

one = [hansu[0],0]
two = [hansu[0],right_up[1]]
three = [0, hansu[1]]
four = [right_up[0],hansu[1]]

dots = [one,two,three,four]
distances = list()
for x in dots:
    distance = ((hansu[0] - x[0])**2 + (hansu[1] - x[1])**2)**(1/2)
    distances.append(distance)
    

distances.sort()
print(int(distances[0]))
    