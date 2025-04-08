scores = [30,50,80,60,90]

# print(sum(scores),max(scores),min(scores))
# print(len(scores))
# print(60 in scores)

# #查詢 : 查東西[key] ->0 ~ 4
# print(scores[4])
# print(scores[len(scores)-1]) #很醜
# print(scores[-1])

# #查詢一段
# # scores = [30,50,80,60,90]
# print(scores[2:5]) #不包含最後一個2、3、4
# print(scores[1:-1]) #包含最後一個-1是倒數，1、2、3
# print(scores[:3]) #0、1、2 從第一個開始
# print(scores[1:])#1、2、3、4 到最後一個

# #跳號操作
# print(scores[0:5:2]) #開始:結束的前一個:跳幾號
# print(scores[::2],scores[1::2]) #從頭到結束2個一跳奇數
# #從1到結束兩個一跳 偶數

#反向跳號(從右跳左)
print(scores[-1::-2])#-1、-3、-5
print(scores[4:0:-2]) #4、2 "0不包含"
print(scores[::-1]) #-1、-2、-3、-4、-5