def find_number(x):
    if x >= 0 and x <= 2:
        result_num = 2
    elif x >= 3 and x <= 5:
        result_num = 3 
    elif x >= 6 and x <= 8:
        result_num = 4
    elif x >= 9 and x <= 11:
        result_num = 5
    elif x >= 12 and x <= 14:
        result_num = 6
    elif x >= 15 and x <= 18:
        result_num= 7
    elif x >= 19 and x <= 21:
        result_num = 8
    else:
        result_num = 9
        
    return result_num

def cal_total_time(result_number):
    total_time = 0 
    for x in result_number:
        total_time = total_time + int(x)
    total_time = total_time + len(result_number)
        
    return total_time
        



if __name__ == "__main__":   
    alpas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    grandmas_num = input()
    result_number = list()
    for x in grandmas_num:
        xs_location = alpas.index(x)
        get_number = find_number(xs_location)
        result_number.append(get_number)
        
    total_time = cal_total_time(result_number)
    print(total_time)
    
    


    