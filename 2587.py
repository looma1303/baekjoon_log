data = list()
for x in range(0,5):
    q = int(input())
    data.append(q)
    
data.sort()

print(int(sum(data)/5))
print(data[2])
    