from pathlib import Path
import pandas as pd


def main():
    # 讀取學生編號與姓名的CSV檔案
    path1 = Path("Ex11", "Ex11_3_1.csv")
    df1 = pd.read_csv(path1, delimiter=r"\s*,\s*", engine="python")

    # 讀取學生編號與成績的CSV檔案
    path2 = Path("Ex11", "Ex11_3_2.csv")
    df2 = pd.read_csv(path2)

    # 依據'No'欄位合併兩個DataFrame
    merged_df = pd.merge(df1, df2, on="No")
    # 顯示合併後的DataFrame
    print(merged_df)

    # 將合併後的DataFrame存入CSV檔案
    # index=False則產生的CSV檔案不會有index
    path_write = Path("Ex11", "Ex11_3_result.csv")
    merged_df.to_csv(path_write, index=False)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")

