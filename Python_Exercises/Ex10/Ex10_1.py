from pathlib import Path
import numpy as np


def main():
    # 設定輸入檔案名稱
    input_file = Path("Ex10", "Ex10_1.csv")

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
    # print(f"data:\n{data}")

    for studentArray in data:
        for attribute in studentArray:
            print(f"{attribute}", end="\t")
        print()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
