n = input()
n = list(n)
del_pos = list()
split_list = list()


    
    
def split_str(a):
    global split_list
    global q
    global n
    for x in range(0, len(n)):
        if len(n) == 1:
            split_list.append(str(n[x]))
            del n[x]
            q = q + 1
            break
            
        elif n[x] == 'c':
            if n[x + 1] == '=' or n[x + 1] == '-':
                split_list.append(str(n[x])+str(n[x+1]))
                del n[x]
                del n[x]
                q = q + 1
                break
            else:
                split_list.append(str(n[x]))
                del n[x]
                q = q + 1
                break
            
            
        elif n[x] == 'd':
            if n[x + 1] == 'z':
                if len(n) == 2:
                    split_list.append(str(n[x]))
                    del n[x]
                    q = q + 1
                    break
                    
                elif n[x + 2] == '=':
                    split_list.append(str(n[x])+str(n[x+1])+str(n[x+2]))
                    del n[x]
                    del n[x]
                    del n[x]
                    q = q + 1
                    break 
                else:
                    split_list.append(str(n[x]))
                    del n[x]
                    q = q + 1
                    break
                
                
            elif n[x + 1] == '-':
                split_list.append(str(n[x])+str(n[x+1]))
                del n[x]
                del n[x]
                q = q + 1
                break
            else:
                split_list.append(str(n[x]))
                del n[x]
                q = q + 1
                break
                    
        elif n[x] == 'l':
            if n[x + 1] == 'j':
                split_list.append(str(n[x])+str(n[x + 1]))
                del n[x]
                del n[x]
                q = q + 1 
                break
            else:
                split_list.append(str(n[x]))
                del n[x]
                q = q + 1
                break
            
                        
        elif n[x] == 'n':
            if n[x + 1] == 'j':
                split_list.append(str(n[x]+str(n[x+1])))
                del n[x]
                del n[x]
                q = q + 1 
                break
            else:
                split_list.append(str(n[x]))
                del n[x]
                q = q + 1
                break
                            
        elif n[x] == 's':
            if n[x + 1] == '=':
                split_list.append(str(n[x])+str(n[x + 1]))
                del n[x]
                del n[x]
                q = q + 1 
                break
            else:
                split_list.append(str(n[x]))
                del n[x]
                q = q + 1
                break
                
                
        
        elif n[x] == 'z':
            if n[x + 1] == '=':
                split_list.append(str(n[x])+str(n[x + 1]))
                del n[x]
                del n[x]
                q = q + 1
                break
            else:
                split_list.append(str(n[x]))
                del n[x]
                q = q + 1
                break
            
        else:
            split_list.append(str(n[x]))
            del n[x]
            q = q + 1
            break
        
    return q



q = 1
a = 0

while q == 1:
    q = 0
    split_str(a)
    
print(len(split_list))
    