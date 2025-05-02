import numpy as np


def main():
    # 輸入學生數
    num_students = int(input("請問有幾個學生? "))

    # 建立空的學生資料列表
    students = []

    # 依序輸入學生資料
    for i in range(num_students):
        data = input(f"請輸入第{i + 1}個學生名與國、英、數成績: ").split()
        students.append(data)

    print("輸入完畢!")

    # 將資料轉為 NumPy 陣列
    students_array = np.array(students)

    # 查詢學生資料
    query_name = input("請輸入欲查詢的學生名: ").strip().lower()

    # 搜尋符合的學生
    found = False
    for student in students_array:
        name = student[0]
        # 比對局部名稱
        if query_name in name.lower():
            found = True
            # 將學生名與成績列出
            print(name, end=" ")
            for i in range(1, len(student)):
                print(student[i], end=" ")
            print()

    if not found:
        print("查無此學生!")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
# --------------------------------------------------
# c=[] 

# n = int(input("有幾個學生"))

# for range(n):
#     b = input("學生資料")
#     c = b.append

# def search(name):
#     if name in  c:
#         print({c})

# c = []  # ✅ OK，這是用來裝學生資料的清單

# n = int(input("有幾個學生"))  # ✅ OK

# for range(n):  # ❌ 錯：for 要搭配變數，應該是：for i in range(n)
#     b = input("學生資料")  # ✅ OK，輸入格式可以是：Alice 80 90 85
#     c = b.append  # ❌ 錯：你這樣是把「append 函式」存進 c，不是把 b 加進 c

# def search(name):
#     if name in  c:  # ❌ 錯：c 裡面是學生整串字，不是單純名字；要先分開處理
#         print({c})  # ❌ 錯：你是要印特定學生資料，不是整包印出來
# ---------------------------------------------------------------------------
students = []

n = int(input("有幾個學生？"))

# 資料輸入：每筆資料包含姓名與成績
for i in range(n):
    raw = input(f"請輸入第{i+1}個學生資料（格式：姓名 國 英 數）: ")
    parts = raw.split()  # 切成 list，例如 ['Alice', '80', '90', '85']
    name = parts[0]
    scores = list(map(int, parts[1:]))
    students.append([name] + scores)  # 存成 ['Alice', 80, 90, 85]

# 查詢函式
def search(name):
    found = False
    for student in students:
        if student[0].lower() == name.lower():
            print(f"{student[0]} {student[1]} {student[2]} {student[3]}")
            found = True
            break
    if not found:
        print("查無此人")

# 查詢測試
query = input("請輸入要查詢的學生名字：")
search(query)
