n = input()
n = int(n)
if n == 1:
    exit()
result = list()


def loop(n):
    global result
    for x in range(2, n + 1):
        if n % x == 0:
            result.append(x)
            n = n / x
            break
        else:
            pass
    return int(n)
            

while True:
    if n == 1:
        break
    else:
        n = loop(n)
        
for x in result:
    print(x)