import numpy as np


def main():
    # 使用者輸入學生人數
    num_students = int(input("請問有幾個學生? "))

    names = []
    scores = []

    # 依序輸入學生資料
    for i in range(num_students):
        student_input = input(f"請輸入第{i + 1}個學生名與國、英、數成績: ")
        student_info = student_input.split()

        # 解析輸入的學生資料
        names.append(student_info[0])
        scores.append(list(map(int, student_info[1:])))

    # 將學生成績轉換為ndarray
    student_scores = np.array(scores)
    ## 計算總分、平均 ##
    # 每列總和
    totals = student_scores.sum(axis=1)
    # print(f"totals: {totals}")
    # 每列平均
    averages = student_scores.mean(axis=1)
    # print(f"averages: {averages}")

    # 合併結果(相同index的值會合併成一列)
    results = np.column_stack((names, totals, averages))
    print(f"結果:\n{results}")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
