import random

low , high = 1 , 100
ans = random.randint(1,100)
#假設答案是87

while True :
    while True:
        print("請輸入",low,"-",high,":")
        guess = int(input())
        if low <guess< high:
            break
        else:
            print("數字錯誤")

        if guess <ans:
            print("猜小了")
            low = guess 
        elif guess > ans :
            print("猜大了")
            high = guess 
        else :
            print("恭喜猜對")
            break
    
