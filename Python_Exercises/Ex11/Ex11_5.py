from pathlib import Path
import pandas as pd
from pandas import DataFrame


def discound_sort(df: DataFrame, discount):
    df["price"] *= 1 - discount
    # 價格升冪排序
    df_result = df.sort_values(by="price")
    print("df_result:\n", df_result)

    # 將結果存成CSV檔
    path_write = Path("Ex11", "Ex11_5_result.csv")
    df_result.to_csv(path_write, index=False)


def main():
    path = Path("Ex11", "Ex11_5.csv")
    df = pd.read_csv(path, delimiter=r"\s*,\s*", engine="python")
    print("df:\n", df)
    print("===================================")
    discound_sort(df, 0.2)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
