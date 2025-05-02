# import numpy as np


# def main():
#     # 使用者輸入學生人數
#     num_students = int(input("請問有幾個學生? "))

#     names = []
#     scores = []

#     # 依序輸入學生資料
#     for i in range(num_students):
#         student_input = input(f"請輸入第{i + 1}個學生名與國、英、數成績: ")
#         student_info = student_input.split()

#         # 解析輸入的學生資料
#         names.append(student_info[0])
#         scores.append(list(map(int, student_info[1:])))

#     # 將學生成績轉換為ndarray
#     student_scores = np.array(scores)
#     ## 計算總分、平均 ##
#     # 每列總和
#     totals = student_scores.sum(axis=1)
#     # print(f"totals: {totals}")
#     # 每列平均
#     averages = student_scores.mean(axis=1)
#     # print(f"averages: {averages}")

#     # 合併結果(相同index的值會合併成一列)
#     results = np.column_stack((names, totals, averages))
#     print(f"結果:\n{results}")


# if __name__ == "__main__":
#     print("===================================")
#     main()
#     print("===================================")
# --------------------------------------------------------

# a = []

# student_number = int(input("請問有幾個學⽣?"))
# for i in range(student_number):
#     b = str(input(f"請輸入第{i}個學⽣名與國、英、數成績: "))
#     a = b.append()
#     for element in range(b):
#         str(a[0])
    
#     b = str(input(...))           # 其實不需要 str()，input 本來就是字串
#     a = b.append()                # ❌ 錯：b 是字串，不能用 .append()，而且你要把東西加到 list a 裡面
#     for element in range(b):      # ❌ 錯：b 是字串，不能用在 range 裡面
#     str(a[0])                     # ❌ 這句意義不明，沒存東西也沒輸出

# ---------------------------------------------------------------
a = []

student_number = int(input("請問有幾個學生? "))

for i in range(student_number):
    # 輸入資料並分割
    raw = input(f"請輸入第{i + 1}個學生名與國、英、數成績: ")
    parts = raw.split()  # 例如：['Alice', '80', '90', '85']

    name = parts[0]
    scores = list(map(int, parts[1:]))  # 把成績轉成整數

    total = sum(scores)
    average = total / len(scores)

    # 儲存格式 ['Alice', '255', '85.0']
    a.append([name, str(total), str(round(average, 1))])

print("結果:")
for student in a:
    print(student)

