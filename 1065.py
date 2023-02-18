#import pdb

def checker(num):
    if len(num) == 1 or len(num) == 2:
        state = 'Y'
    else:
        gap = num[0] - num[1]
        #pdb.set_trace()
        for z in range(1,len(num)+1):
            #print(z)
            try:
                
                if num[z-1] - num[z] == gap:
                    
                    state = 'Y'
                else:
                    
                    state = 'N'
                    break
            except:
                state = 'Y'
                

    return state



if __name__ == '__main__':
    n = input()
    result = 0
    for x in range(1, int(n)+1):
        num = []
        for y in str(x):
            num.append(int(y))
        state = checker(num)
        if state == 'Y':
            result = result + 1
        else:
            pass

    print(result)

        



    
