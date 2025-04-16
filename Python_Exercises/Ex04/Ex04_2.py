myFriends = list()
number = int(input("請問有幾個好友? "))
for i in range(number):
    name, cash = input(f"請輸入第{i + 1}個好友名與身上現金: ").split()
    myFriends.append({"name": name, "cash": int(cash)})

count = 0
borrow = int(input("請輸入欲借現金: "))
print("可借錢的好友: ", end="")
for friend in myFriends:
    if friend["cash"] >= borrow:
        print(friend["name"], end=", ")
        count += 1

print(f"共{count}人")
