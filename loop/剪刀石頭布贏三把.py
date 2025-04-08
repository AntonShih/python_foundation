import random

win , lose = 0 , 0

while win <3 and lose<3:
    #-1就是我輸 0就是平手 1就是我贏
    #我還沒贏三次而且對手還沒贏三次就要繼續，條件以外就結束迴圈
    result = random.randint(-1,1)
    print(result)
    if result == -1:
        lose = lose +1
    elif result == 1:
        win = win + 1

if win>lose:
    print("遊戲結束，我贏了")
else:
    print("遊戲結束，你贏了")