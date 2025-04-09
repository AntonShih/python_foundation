import random

n = 3
total = 100000
win , lose = 0 , 0

for i in range(total):

    # 先準備n個門 [1和0] 0沒獎 1有獎
    
    doors =[0]*(n-1)
    # idx = random.randint(0,n-1) #0-3
    idx = random.randint(0,len(doors)-1)

    #insert (插入位置，插入值)
    doors.insert(idx,1) #1代表有獎
    # print("準備的門",doors) 

    #隨機選一個門random
    chose = random.randint(0,len(doors)-1) #int
    # print(type(chose),chose)
    # # print("選到的門:",doors[chose])

    #pop(idx) 刪除idx位置 pop()刪除最後一個
    doors.pop(chose)
    # print("剩下的門:",doors)
    #在剩下的門裡面，主持人開一個沒獎的
    #remove (值) :從左到右
    doors.remove(0)
    # print("剩下的門:",doors)


    #扣除剛剛那兩道以後，再帶一道回家
    chose = random.randint(0,len(doors)-1)
    if doors[chose] == 1:
        # print("你中獎了" )
        win = win + 1
    else :
        # print("你沒中獎")
        lose = lose + 1

ratio = win / total
print("贏的機率是:",ratio)