num = input()
n = input()
n = n.split()
a = int(input())
b = list()
result = 0
for x in n:
    b.append(int(x))
    
for x in b:
    if x == a:
        result = result + 1
        
print(result)
        
    