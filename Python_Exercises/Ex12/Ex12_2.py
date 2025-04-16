from pandas import DataFrame


def main():
    data = {
        'Category': ['A', 'B', 'A', 'B', 'C', 'A', 'C', 'B'],
        'Amount': [100, 200, 150, 300, 250, 50, 400, 100],
        'Quantity': [2, 4, 3, 6, 5, 1, 8, 2]
    }
    df = DataFrame(data)
    print(df)
    print("-----------------------------------")

    print("使用 groupby 進行分組統計:")
    result = df.groupby('Category').agg(
        Total_Amount=('Amount', 'sum'),  # 計算總銷售金額
        Average_Quantity=('Quantity', 'mean')  # 計算平均銷售數量
    ).reset_index()

    print(result)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")

