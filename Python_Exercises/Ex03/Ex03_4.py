# count = 0
# text = ""
# unluck = 4

# while True:
#     unluck = int(input("不吉利數字 (1 ~ 9) : "))
#     if unluck < 1 or unluck > 9:
#         print("輸入錯誤，請再輸入一次")
#         continue
#     else:
#         break


# for number in range(1, 49 + 1):
#     if number // 10 == unluck or number % 10 == unluck:
#         continue
#     count += 1
#     if number < 10:
#         text += "0"
#     text += f"{number} "

#     if count % 10 == 0:
#         text += "\n"

# text += f"\n總個數: {count}"
# print(text)

# ----------------------------------------------------------------



# while True:
#     unluck = int(input("輸入不幸運的數字1-9:"))
#     if unluck <0 or unluck >9:
#         print("請重新輸入不幸運數字:")
#     else :
#         break

# unluck = str(unluck)  # 為了比對字串（像 '4'）
# count = 0

# for i in range(1, 50):
#     if unluck in str(i):
#         continue
#     print(f"{i:02}", end=" ")
#     count += 1
#     if count % 10 == 0:
#         print()  # 每十個換行

# print(f"\n總個數: {count}")

# ------------------------------------------------------------
count = 0

while True:
    unluck = int(input("輸入不幸運的數字1-9:"))
    if unluck <1 or unluck>9:
        print("請重新輸入不幸運數字:")
    else :
        break

print(f"不幸運的數字1-9:{unluck}")

for i in range(1,49+1):
    if i // 10 == unluck or i % 10 == unluck:
        continue

    print(f"{i:02}", end=" ")
    count += 1

    if count % 10 == 0:
        print()

print(f"\n總個數: {count}")