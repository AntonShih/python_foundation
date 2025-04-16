from pathlib import Path
import pandas as pd


def main():
    path = Path("Ex11", "Ex11_4.csv")
    df = pd.read_csv(path, delimiter=r"\s*,\s*", engine="python")
    print("df:\n", df)
    print("-----------------------------------")

    # 刪除姓名為空值者
    df = df.dropna(subset=["Name"])

    # 刪除姓名重複且國、英、數成績有空值者
    # 將成績降冪排序，空值就會排在後面而被移除(keep參數預設為'first')
    df = df.sort_values(
        by=["Chinese", "English", "Math"], ascending=False
    ).drop_duplicates(subset=["Name"])

    # 國、英、數成績為空值者，值改為0
    df[["Chinese", "English", "Math"]] = df[
        ["Chinese", "English", "Math"]].fillna(0)

    # 國、英、數成績不在0 ~ 100範圍內的改為0
    df[["Chinese", "English", "Math"]] = df[
        ["Chinese", "English", "Math"]].map(
            lambda x: x if 0 <= x <= 100 else 0)

    # index升冪排序
    df_result = df.sort_index()
    print("df_result:\n", df_result)
    
    # 將結果存成CSV檔
    path_write = Path("Ex11", "Ex11_4_result.csv")
    df_result.to_csv(path_write, index=False)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")

