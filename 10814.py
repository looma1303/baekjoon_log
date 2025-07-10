n = int(input())
data_list = list()
for x in range(0,n):
    data = input()
    data = data.split()
    data_list.append([int(data[0]), data[1]])
    
    
result = sorted(data_list, key = lambda x:x[0])

for x in result:
    print(x[0], x[1])