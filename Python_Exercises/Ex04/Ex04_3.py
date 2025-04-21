# import random

# lotterySet = set()
# # 大樂透號碼總共有6個號碼加1個特別號
# lotteryCount = 6 + 1
# while len(lotterySet) < lotteryCount:
#     # 隨機產生一個1~49的號碼
#     number = random.randint(1, 49)
#     lotterySet.add(number)

# # set轉成list方便移除指定元素與排序
# lotteryList = list(lotterySet)
# # 將最後一個號碼取出當作特別號碼
# special = lotteryList.pop()
# print("開獎，大樂透號碼為: ")
# for number in lotteryList:
#     print(number, end=" ")
# print(f"特別號: {special}")

# # 排序
# lotteryList.sort()
# print("由小到大排列:")
# for number in lotteryList:
#     print(number, end=" ")
# print(f"特別號: {special}")
# ----------------------------------------------------------------
# import random ##錯誤會重複!!!
# numbers = []

# for i in range(6+1):
#     number = random.randint(1,49+1)
#     numbers.append(number)
# sp = numbers[random.randint(0,len(numbers)-1)]
# # sp = random.choice(numbers) 

# numbers.remove(sp)     # 把特別號從原始 list 移除
# numbers.sort()         # 將剩下的主號排序
# print("主號：", numbers)
# print("特別號：", sp)

# # b = numbers.remove[sp].sort
# remove()


# --------------------------------------------------------------
import random

# 產生 7 個不重複的號碼
numbers = random.sample(range(1, 50), 7)

# 隨機抽出一個當特別號
sp = random.choice(numbers)

# 剩下的號碼就是主號（排序）
main_numbers = numbers.copy()
# main_numbers = numbers
# 那你只是讓兩個變數「指向同一個記憶體」，
# 只要你改了 main_numbers，numbers 也會被改到。
main_numbers.remove(sp)
main_numbers.sort()

print("主號：", main_numbers)
print("特別號：", sp)
# -------------------------------------------------------
import random

numbers = []

while len(numbers) < 7:
    number = random.randint(1, 49)
    if number not in numbers:   # 確保不重複才加入
        numbers.append(number)

sp = random.choice(numbers)     # 抽出特別號
numbers.remove(sp)              # 主號排除特別號
numbers.sort()

print("主號：", numbers)
print("特別號：", sp)
