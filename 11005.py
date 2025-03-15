data = input()
data = data.split()
data[0] = int(data[0])
data[1] = int(data[1])
result = list()
num = data[0]
zinbup = data[1]

alpz = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

while True:
    if num % zinbup > 9:
        result.insert(0,alpz[num % zinbup - 10])
    else:
        result.insert(0,str(num % zinbup))
    num = num // zinbup
    if num == 0:
        break
        
        

        
        
if len(result) > 1:
    print(''.join(result))
else:
    print(result[0])