from pandas import DataFrame


def main():
    # 輸入學生數
    num_students = int(input("請問有幾個學生? "))

    # 建立空的學生資料列表
    students = []

    # 依序輸入學生資料
    for i in range(num_students):
        data = input(f"請輸入第{i + 1}個學生名與國、英、數成績: ").split()
        name = data[0]
        # 將成績轉為整數
        scores = list(map(int, data[1:]))
        students.append([name] + scores)

    # 將資料轉為 DataFrame
    df = DataFrame(students, columns=["Name", "Chinese", "English", "Math"])
    print("\n學生資料輸入完畢如下:")
    print(df)

    # 查詢學生資料
    query_name = input("\n請輸入欲查詢的學生名: ").strip().lower()
    # DataFrame.str允許DataFrame的字串欄位直接呼叫字串函式，且適用於整列資料
    # na=False：如果Name欄位有NaN不會報錯，而是將NaN視為False(不匹配)
    result = df[df["Name"].str.lower().str.contains(query_name, na=False)]
    if not result.empty:
        print("查詢結果:")
        print(result)
    else:
        print("\n查無此學生!")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")

