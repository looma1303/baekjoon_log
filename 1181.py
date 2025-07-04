n = int(input())
words = list()
for x in range(0,n):
    q = input()
    if q in words:
        pass
    else:
        words.append(q)
    
words.sort(key=lambda word:(len(word), word))
for x in words:
    print(x)