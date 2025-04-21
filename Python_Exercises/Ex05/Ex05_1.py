# def calculate(numbers):
#     numSum = 0
#     for num in numbers:
#         numSum += num
#     average = numSum / len(numbers)
#     return numSum, average


# def main():
#     numList = []
#     inputStr = input("請輸入整數數列(空白分隔): ")
#     print(f"數列為: {inputStr}")
#     strList = inputStr.split()
#     for s in strList:
#         numList.append(int(s))
#     result = calculate(numList)
#     print(f"總和 = {result[0]}")
#     print(f"平均 = {result[1]}")


# main()
# ------------------------------------------------------------------

# def calculate(*numbers):
#     a=0
#     for i in numbers:
#         a += i
#         avrage = a/len(numbers)
#     print(f"數列為{numbers}")
#     return(a,avrage)

# # b= []
# # b = int(input("請輸入整數數列(空⽩分隔):").split())
# # ###不能這樣寫要用map
# # calculate(b)

# -----------------------------------------------

def calculate(*numbers):
    a = 0
    for i in numbers:
        a += i
    average = a / len(numbers)
    print(f"數列為 {numbers}")
    return a, average

# 處理輸入字串：切割 + 轉整數 + 變成 list
user_input = input("請輸入整數數列（空白分隔）：")
b = list(map(int, user_input.split()))

# 使用 * 將 list 展開成多個參數傳進去
total, avg = calculate(*b)

print(f"總和：{total}")
# 不能直接接a, average會報錯
print(f"平均：{avg:.2f}")
# ------------------------------------------------------------
def calculate(*numbers):
    a = 0  # 總和變數放這裡
    for i in numbers:
        a += i
    average = a / len(numbers)
    print(f"數列為 {numbers}")
    return a, average

# 取得使用者輸入並處理成整數 tuple
user_input = input("請輸入整數數列（空白分隔）：")
int_list = list(map(int, user_input.split()))

# 用 * 解包傳進函式
total, avg = calculate(*int_list)

print(f"總和為：{total}")
print(f"平均為：{avg:.2f}")
