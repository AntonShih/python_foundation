a,b = 3,5
ans = '0.'
i = 0
while i<10:
    #2->20
    a10 = a * 10
    #30 // 5(//取商)
    ans = ans + str(a10 // b)#要改變一定要設定回去
    print (ans)
    # 20 % 7 #(%取餘數)
    a = a10 % b
    if a == 0:
        break
    i = i + 1