import random

win , lose = 0 , 0

while True:
    #-1就是我輸 0就是平手 1就是我贏
    #我還沒贏三次而且對手還沒贏三次就要繼續，條件以外就結束迴圈
    result = random.randint(-1,1)
    print(result)
    if result == -1:
        lose = lose +1
    elif result == 1:
        win = win + 1
    if win == 3:
        print("win")
        break
    elif lose == 3:
        print("lose")
        break
