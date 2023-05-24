def return_reversed_list(i,j,num_list,N):
    if i == 1 and j == N:
        sample_list = num_list[i-1:j]
        #front_list = num_list[:i-1]
        #back_list = num_list[j-1:]
        sample_list.reverse()
        return (sample_list)
    elif i == 1:
        sample_list = num_list[i-1:j]
        #front_list = num_list[:i-1]
        back_list = num_list[j:]
        sample_list.reverse()
        return (sample_list + back_list)
    elif j == N:
        sample_list = num_list[i-1:j]
        front_list = num_list[:i-1]
        #back_list = num_list[j-1:]
        sample_list.reverse()
        return (front_list + sample_list)
        
        
    else:
        sample_list = num_list[i-1:j]
        front_list = num_list[:i-1]
        back_list = num_list[j:]
        sample_list.reverse()
        return (front_list + sample_list + back_list)  
    
      

n = input()

n = n.split()
for x in range(0,2):
    n[x] = int(n[x])


N = n[0]
M = n[1]
num_list = list()
for x in range(1,N+1):
    num_list.append(x)
    
    

for x in range(0,M):
    b = input()
    b = b.split()
    for x in range(0,2):
        b[x] = int(b[x])

    i = b[0]
    j = b[1]
    if i == j:
        pass
    else:
        num_list = return_reversed_list(i,j,num_list,N)
        #print(num_list)
    

    

for x in num_list:
    print(x, end = " ")
    
    


#i부터 j까지 reverse

    
