n = input()
n = n.split()
box_num = int(n[0])
ball_times = int(n[1])
boxes = list()
for x in range(0,box_num):
    boxes.append(0)
    
for x in range(0,ball_times):
    a = input()
    a = a.split()
    for y in range(int(a[0])-1,int(a[1])):
        boxes[y] = int(a[2])
        
    #print(boxes)
    
for x in range(0,len(boxes)):
    boxes[x] = str(boxes[x])
    
result = ' '.join(boxes)
print(result)
        

