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
