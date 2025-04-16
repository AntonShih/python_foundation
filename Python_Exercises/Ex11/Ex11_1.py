from pathlib import Path
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


def load_df_csv(path):
    # 載入CSV檔案，預設分隔符號為","，可使用正規表示式設定分隔符號
    # 建議設定engine="python"；因為預設為engine="c"，沒有支援正規表示式
    df_csv = pd.read_csv(
        path,
        delimiter=r"\s*,\s*",
        engine="python"
    )
    return df_csv


def barChart(df):
    df_melted = df.melt(id_vars="Name", var_name="Subject", value_name="Score")
    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_melted, x="Name", y="Score", hue="Subject")
    # 圖例原錨點位置在(0, 0)，就是在圖表的左下方
    # bbox_to_anchor=(0, 1): 代表圖例新的錨點位置設在圖表左上方邊界
    # loc="upper right": 代表圖例的右上端對齊新的錨點(所以圖例會在錨點左下方)
    # 以下設定就不會讓圖例遮蔽圖表資訊
    plt.legend(bbox_to_anchor=(0, 1), loc="upper right")
    plt.title("Students' Scores by Subject")
    plt.show()


def main():
    # 欲載入的檔案路徑
    path = Path("Ex11", "Ex11_1.csv")
    df_csv = load_df_csv(path)
    print(f"載入檔案內容如下:\n{df_csv}")

    barChart(df_csv)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
