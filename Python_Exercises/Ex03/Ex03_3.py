start = int(input("起始值: "))
end = int(input("終止值: "))
text = ""
total = 0
count = 0

for number in range(start, end + 1):
    total += number
    count += 1
    if number < 10:
        text += "0"
    text += f"{number} "

    if count % 10 == 0:
        text += "\n"

text += f"\n總和: {total}"
print(text)

# ----------------------------------------------------------------------
# start = int(input("請輸入起始值："))
# end = int(input("請輸入終止值："))

# total = 0  # 用來累加總和
# count = 0  # 控制每行輸出 10 個

# for i in range(start, end + 1):
#     print(f"{i:02}", end=" ")  # 格式化為兩位數，例如 01、02...
#     total += i
#     count += 1
#     if count % 10 == 0:
#         print()  # 每 10 個換行

# print(f"\n總和: {total}")