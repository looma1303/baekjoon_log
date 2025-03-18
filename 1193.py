n = input()
n = int(n)
arry_len = 1
if n == 1:
    print('1/1')
else:
    while True:
        if n  <= arry_len:
            if arry_len % 2 == 0:
                way = 'down' #짝수는 진행 방향이 아래.
                point = [1, arry_len]
            else:
                way = 'up'
                point = [arry_len, 1]
            while True:
                if n == 0:
                    break
                else:
                    if way == 'down':
                        point[0] = point[0] + 1
                        point[1] = point[1] - 1
                        n = n - 1
                    else:
                        point[0] = point[0] - 1
                        point[1] = point[1] + 1
                        n = n - 1

            break

        else:
            n = n - arry_len
            arry_len = arry_len + 1 #포함되는 극단을 만날때까지 빼기.
        
    print(point)