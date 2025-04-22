def calculate(numbers, myFunction):
    myFunction(numbers)


def main():
    numList = []
    inputStr = input("請輸入整數數列(空白分隔): ")
    print(f"數列為: {inputStr}")
    strList = inputStr.split()
    for s in strList:
        numList.append(int(s))

    def myAverage(numbers):
        numSum = 0
        for num in numbers:
            numSum += num
        print(f"平均 = {numSum / len(numbers)}")

    calculate(numList, myAverage)


main()

# -----------------------------------------------------------

# def calculate(*numbers, myFunction) :
#     print(f"數列為:{numbers}")

# def myFunction():
#     b = a/len(a)
#     print(f"平均={b}")

# calculate(a = map(int,input("請輸入整數數列(空⽩分隔):")),myFunction)
# ------------------------------------------------------------
def calculate(numbers, myFunction):
    print(f"數列為: {numbers}")
    myFunction(numbers)  # 呼叫你傳進來的功能函式，並把資料丟進去

# 自定義功能函式：計算平均
def myFunction(numbers):
    average = sum(numbers) / len(numbers)
    print(f"平均 = {average:.2f}")

# 使用者輸入並轉成整數 list
user_input = input("請輸入整數數列（空白分隔）：")
a = list(map(int, user_input.split()))

# 執行主功能
calculate(a, myFunction)
# -----------------------------------------------------------
# *numbers 是可變參數
# 如果你想要讓 calculate 接無限多個數字，也可以寫成：
def calculate(myFunction, *numbers):
    print(numbers)
    myFunction(numbers)

# 但你要呼叫的時候就要寫成：
# calculate(myFunction, 10, 20, 30)

