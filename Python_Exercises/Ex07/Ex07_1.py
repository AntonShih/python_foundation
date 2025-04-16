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
