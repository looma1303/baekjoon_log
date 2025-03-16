n = input()
n = int(n)


rectangle = 1
dot = 4
line = 4
dup = 1



def algo(rectangle, line ,dot):
    rectangle = rectangle * 4
    line = rectangle * 4 - (rectangle)
    dot = line - (line / 4)
    print(rectangle, line, dot)
    return(rectangle, line, dot)

for x in range(0, n):
    rectangle, line, dot = algo(rectangle, line, dot)
    
print(dot)