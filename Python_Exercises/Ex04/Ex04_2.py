# myFriends = list()
# number = int(input("請問有幾個好友? "))
# for i in range(number):
#     name, cash = input(f"請輸入第{i + 1}個好友名與身上現金: ").split()
#     myFriends.append({"name": name, "cash": int(cash)})

# count = 0
# borrow = int(input("請輸入欲借現金: "))
# print("可借錢的好友: ", end="")
# for friend in myFriends:
#     if friend["cash"] >= borrow:
#         print(friend["name"], end=", ")
#         count += 1

# print(f"共{count}人")


# ----------------------------------------------------------
# friend_number = int(input("請問有幾個好友?"))

# # def who()
# for i in range(1,friend_number+1):
#     input(f"請輸入第{i}個好友名與⾝上現⾦:")
# --------------------------------------------------------------
myFriends = []
number = int(input("請問有幾個好友? "))

for i in range(number):
    name, cash = input(f"請輸入第{i + 1}個好友名與身上現金: ").split()
    myFriends.append({"name": name, "cash": int(cash)})

borrow = int(input("請輸入欲借現金: "))

# 篩選出符合條件的好友
canBorrow = [friend["name"] for friend in myFriends if friend["cash"] >= borrow]

if canBorrow:
    print("可借錢的好友:", ", ".join(canBorrow))
else:
    print("沒有好友可以借你這麼多錢 😅")

print(f"共 {len(canBorrow)} 人")
