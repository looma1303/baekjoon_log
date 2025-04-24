n = input()
n = int(n)
x_data = list()
y_data = list()
for x in range(0,n):
    q = input()
    q = q.split()
    x_data.append(int(q[0]))
    y_data.append(int(q[1]))
    
x_data.sort()
y_data.sort()

x_lowest = x_data[0]
y_lowest = y_data[0]
x_highest = x_data[len(x_data)-1]
y_highest = y_data[len(y_data)-1]

result = (x_highest - x_lowest) * (y_highest - y_lowest)
print(result)
    