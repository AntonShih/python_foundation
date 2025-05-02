from pathlib import Path
import numpy as np


def main():
    # 設定輸入與輸出檔案名稱
    input_file = Path("Python_Exercises/Ex10", "Ex10_4.csv")
    output_file = Path("Python_Exercises/Ex10", "Ex10_4_result.csv")

    # 讀取成績單csv檔，並跳過第一列標題
    data = np.genfromtxt(
        input_file,
        # 分隔符號，預設為空白字元
        delimiter=",",
        # 設定結果陣列的資料類型，如不設定會依照各欄位自動推定類型
        dtype=str,
        # 使用當初文字編碼方式來解碼
        encoding="utf-8",
        # 跳過第一列標題
        skip_header=1
    )
    print(f"data:\n{data}")
    print("-----------------------------------")

    ## 分離姓名與成績 ##
    # 取每列的第一欄為學生名
    names = data[:, 0]
    print(f"names:\n{names}")
    print("-----------------------------------")
    # 取每列後三欄為成績，並轉為浮點數以便計算
    scores = data[:, 1:].astype(float)
    print(f"scores:\n{scores}")
    print("-----------------------------------")

    ## 計算總分、平均與排名 ##
    # 每列總和
    totals = scores.sum(axis=1)
    print(f"totals:\n{totals}")
    print("-----------------------------------")
    # 每列平均
    averages = scores.mean(axis=1)
    print(f"averages:\n{averages}")
    print("-----------------------------------")

    # 計算正確排名
    # 依據總分高到低用index排序; "-totals"負號表示由大到小排序
    sorted_indices = np.argsort(-totals)
    print(f"sorted_indices:\n{sorted_indices}")
    print("-----------------------------------")
    # 建立一個與sorted_indices相同shape的陣列，並將值設為0
    ranks = np.zeros_like(sorted_indices)
    # 將產生的1~n數列，依照sorted_indices的順序填入ranks
    ranks[sorted_indices] = np.arange(1, len(sorted_indices) + 1)  # 排名從 1 開始
    print(f"ranks:\n{ranks}")
    print("-----------------------------------")

    # 合併結果
    results = np.column_stack((names, totals, averages, ranks))
    print(f"results:\n{results}")
    print("-----------------------------------")

    # 存成新的csv檔
    header = "姓名,總分,平均,排名"
    np.savetxt(
        output_file,
        results,
        delimiter=",",
        # 存檔應保留原值，所以設定"%s"為文字類型。只有顯示時才會格式化小數位數
        fmt="%s",
        header=header,
        # 加在標題前的文字，預設為"#"，可改為空字串
        comments="",
        encoding="utf-8"
    )

    print(f"計算完成，結果已保存到 {output_file}")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
# ---------------------------------------------------------
import numpy as np

def main():
    # 輸入學生人數
    student_number = int(input("請問有幾個學生？ "))

    names = []       # 存學生姓名
    scores = []      # 存每位學生的 [國, 英, 數] 成績

    # 輸入每位學生的資料
    for i in range(student_number):
        raw = input(f"請輸入第 {i+1} 位學生的姓名、國英數成績（空格分隔）: ")
        parts = raw.split()
        name = parts[0]
        score = list(map(int, parts[1:]))

        names.append(name)
        scores.append(score)

    # 轉成 NumPy 陣列做後續計算
    scores = np.array(scores)

    # 計算總分與平均
    totals = scores.sum(axis=1)
    averages = scores.mean(axis=1).round(1)

    # 進階一行排名：找出每位學生的正確排名
    ranks = np.argsort(np.argsort(-totals)) + 1

# # 第一步：對 -totals 做 argsort（由大排到小）
# np.argsort(-totals) → [2, 0, 1, 3]
# 解釋：總分最高的是 index 2，其次是 0，再來是 1，最後是 3

# 第二步：對那個結果再做一次 argsort
# np.argsort([2, 0, 1, 3]) → [1, 2, 0, 3]
# 解釋：代表原本 index 0（Alice）是第 2 名 → 放 1
#                     index 1（Bob）是第 3 名 → 放 2
#                     index 2（Cindy）是第 1 名 → 放 0
#                     index 3（David）是第 4 名 → 放 3

# 最後 +1：因為我們想要排名從「1 開始」，不是從 0
# → [2, 3, 1, 4]

    # 顯示成績表
    print("\n====== 成績總表 ======")
    print(f"{'姓名':<6}{'國文':<4}{'英文':<4}{'數學':<4}{'總分':<6}{'平均':<6}{'名次'}")
    print("-" * 35)

    for i in range(student_number):
        print(f"{names[i]:<6}{scores[i][0]:<4}{scores[i][1]:<4}{scores[i][2]:<4}"
              f"{totals[i]:<6}{averages[i]:<6}{ranks[i]}")

if __name__ == "__main__":
    main()
