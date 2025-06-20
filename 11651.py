n = int(input())
dots = list()
for x in range(0,n):
	q = input()
	q= q.split()
	dots.append((int(q[0]), int(q[1])))
	
		
dots.sort(key=lambda x:(x[1],x[0]))
for x,y in dots:
	print(x,y)
	