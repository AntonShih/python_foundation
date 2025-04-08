a,b = 2,7
ans = '0.'
i = 0
while i < 10:
    #2->20
    a10 = a * 10
    #20 // 7(//取商)
    ans = ans + str(a10 // b)#要改變一定要設定回去
    print (ans)
    # 20 % 7 #(%取餘數)
    a = a10 % b
    i = i + 1