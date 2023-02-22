alps = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = input()
loc_list= list()
#loc = 0
for x in alps:
    loc = 0
    for y in n:
        if x == y:
            loc_result = loc
            break

        else:
            loc_result = -1
            
        loc = loc + 1
        
    loc_list.append(str(loc_result))
    
print(' '.join(loc_list))
            