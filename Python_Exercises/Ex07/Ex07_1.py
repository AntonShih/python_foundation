import math
import random


def prime(num):
    # 數字為1, 2, 3時for迴圈檢查不到，所以直接決定是否為質數
    if num == 1:
        return False
    if num == 2 or num == 3:
        return True
    for factor in range(2, int(math.sqrt(num) + 1)):
        if num % factor == 0:
            return False
    return True


def main():
    count = int(input("想要幾個不重複整數(值為1～100(不含))？ "))
    numbers = random.sample(range(1, 100), k=count)

    for num in numbers:
        print(num, end="")
        if prime(num):
            print(" 是質數")
        else:
            print(" 不是質數")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
# ------------------------------------------------------
# import random

# b =[]
# def deliete(number):
#     while True:
#         b = random.simple(range(1,100),k = number)
#         for i in number:
#             for j in b:
#                 if b % ? =!0:
#                     print("是質數")
#                 else:
#                     print("不是質數")


def main():
    c = int(input("想要幾個不重複整數(值為1～100(不含))？"))
    deliete(c)

if __name__== main:
    main()
# ------------------------------------------------------------
import random

# 判斷是否為質數的函式
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        # n**0.5 → 計算平方根
        # int() → 去掉小數點
        #   因為 range 最後一個數字不會被包含，要補回來
        # 暴力跑到 n-1 快超多！
        if n % i == 0:
            return False
    return True

# 主邏輯：產生亂數並檢查質數
def generate_and_check(number):
    nums = random.sample(range(1, 100), k=number)  # 不重複亂數
    for num in nums:
        if is_prime(num):
            print(f"{num} 是質數")
        else:
            print(f"{num} 不是質數")

# 主程式入口
def main():
    c = int(input("想要幾個不重複整數(值為1～100(不含))？"))
    generate_and_check(c)

if __name__ == "__main__":
    main()
