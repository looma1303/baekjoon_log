data = list()
result = list()
qt = 0.25
dm = 0.1
nk = 0.05

num = input()
num = int(num)

for x in range(0, num):
    get = input()
    get = int(get)
    data.append(get)
    
    

    
for x in data:
    charge = x * 0.01
    qt_coin = round(charge // qt) 
    charge = round(charge % qt,2)
    
    dm_coin = round(charge // dm) 
    charge = round(charge % dm,2)
    
    nk_coin = round(charge // nk) 
    charge = round(charge % nk,2)
    
    
    
    phy_coin = round(charge * 100)
    
    
    coin = [str(qt_coin), str(dm_coin), str(nk_coin), str(phy_coin)]
    
    result.append(coin)
    

for x in result:
    print(' '.join(x))
    
    
    
    
    