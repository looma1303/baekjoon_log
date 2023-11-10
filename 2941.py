n = input()
n = list(n)
del_pos = list()
cro_apl_list = ['c=','c-','dz=','d-','lj','nj','s=','z=']


    
    
def del_str(a):
    global q
    global n
    for x in range(0, len(n)):
        print(x)
        if n[x] == 'c':
            if n[x + 1] == '=' or n[x + 1] == '-':
                del n[x+1]
                q = q + 1
                break
            else:
                pass
        elif n[x] == 'd':
                if n[x + 1] == 'z':
                    if n[x + 2] == '=':
                        del n[x + 1]
                        del n[x + 1]
                        q = q + 1
                        break 
                    else:
                        pass
                elif n[x + 1] == '-':
                    del n[x + 1]
                    q = q + 1
                    break
                else:
                    pass
                    
        elif n[x] == 'l':
            if n[x + 1] == 'j':
                del n[x + 1]
                q = q + 1 
                break
            else:
                pass
            
                        
        elif n[x] == 'n':
            if n[x + 1] == 'j':
                del n[x + 1]
                q = q + 1 
                break
            else:
                pass
                            
        elif n[x] == 's':
            if n[x + 1] == '=':
                del n[x + 1]
                q = q + 1 
                break
        
        elif n[x] == 'z':
            if n[x + 1] == '=':
                del n[x + 1]
                q = q + 1
                break
            else:
                pass
            
        else:
            pass
        
    return q
        

q = 1
a = 0
while q == 1:
    q = 0
    q = del_str(a)
    
print(len(n))