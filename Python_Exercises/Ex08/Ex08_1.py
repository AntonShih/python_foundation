def main():
    while True:
        try:
            dividend = int(input("輸入被除數(整數): "))
            divisor = int(input("輸入除數(整數): "))
            print(
                f"{dividend} ÷ {divisor} = {
                    dividend // divisor} ... {dividend % divisor}"
            )
            break
        except ValueError:
            print(f"被除數或除數格式錯誤，請重新輸入")
        except ZeroDivisionError:
            print(f"除數不可為0，請重新輸入")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")

# ---------------------------------------------------------
def main():
    while True:
        try:
            a = int(input("輸入被除數(整數): "))
            b = int(input("輸入除數(整數):"))
            if b == 0:
                print("除數不可為0，請再重新輸入")
                continue  # 回到while重新輸入
            print(f"a/b = {a/b}")
            break
        except ValueError:
            print("被除數或除數格式錯誤")


# ---------------------------------------------------------
def main():
    while True:
        try:
            a = int(input("輸入被除數(整數): "))
            b = int(input("輸入除數(整數): "))
            if b == 0:
                print("除數不可為0，請再重新輸入")
                continue  # 回到while重新輸入
            print(f"a/b = {a/b}")
            break
        except ValueError:
            print("被除數或除數格式錯誤，請再輸入一次")
