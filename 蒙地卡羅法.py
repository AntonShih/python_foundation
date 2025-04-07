import random 
#要記得的東西就要準備在外面

count = 0
#次數
total = 1000000
i = 0
while i < total :
    #對於這次xy座標如果在園裡面則count 0+1 儲存回count在一次count 1+1存回count
    x = random.uniform(-1 , 1) # = 是設定一個值
    y = random.uniform(-1 , 1)
    if x**2 + y**2 <= 1 :
        count = count + 1
    i = i + 1

#園裡面/全部*參照物面積
a = (count/total)*4
print(a)