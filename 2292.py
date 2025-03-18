n = input()
n = int(n)
n = n - 1
r = 1

if n == 0:
    print(1)
else:
    while True:
        if n - 6 * r <= 0:
            result = r
            break
        else:
            n = n - 6 * r
            r = r + 1
        
    print(result + 1)