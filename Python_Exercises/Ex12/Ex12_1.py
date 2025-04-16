from pathlib import Path
import pandas as pd


def main():
    # 讀取 CSV
    path_read = Path("Ex12", "Ex12_1.csv")
    df = pd.read_csv(path_read, delimiter=r"\s*,\s*", engine="python")
    print(df)
    print("-----------------------------------")

    # 計算總分與平均
    df["Sum"] = df[["Chinese", "English", "Math"]].sum(axis=1)
    df["Average"] = df[["Chinese", "English", "Math"]].mean(axis=1)

    # 計算排名（總分由高到低）
    # method="min"代表相同分數會被賦予相同的最小名次；例如兩個人同分且應排名2、3，則都排2
    df["Rank"] = df["Sum"].rank(ascending=False, method="min").astype(int)
    df = df[["Name", "Sum", "Average", "Rank"]]
    # 顯示結果
    print(df)

    # 儲存結果到 Ex11_5_result.csv
    path_write = Path("Ex12", "Ex12_1_result.csv")
    df.to_csv(path_write, index=False)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
