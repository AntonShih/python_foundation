import random

low , high = 1 , 100
ans = random.randint(1,100)
#假設答案是87

while True :
    print("請輸入",low,"-",high,":")
    guess = int(input())
    # if low< guess <high:
    if guess>low and guess <high:
        
        if guess <ans:
            print("猜小了")
            low = guess 
        elif guess > ans :
            print("猜大了")
            high = guess 
        else :
            print("恭喜猜對")
            break
    else:
        print("不合理的輸入")