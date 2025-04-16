# op_func是函式型參數
def calculate(op_func, num1, num2):
    op_func(num1, num2)


def demo01():
    def divide(dividend, divisor):
        print(f"{dividend} / {divisor} = {dividend / divisor}")

    calculate(divide, 10, 2)


# 常見的函式型參數應用：別人寫好的功能函式，例如按鈕點擊事件處理
def button_click(button, task):
    print(f"偵測到使用者點擊 {button} 按鈕...")
    # 呼叫傳入的欲執行的內容
    task()


def demo02():
    # 當使用者點擊新增按鈕時，新增一筆資料
    def insert():
        print("新增一筆資料...")
        print("新增成功!")

    button_click("新增", insert)


def main():
    demo01()
    print("===================================")
    demo02()


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
