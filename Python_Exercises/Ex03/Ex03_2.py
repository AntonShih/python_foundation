season = input("請輸入你喜愛的季節: ")
match season.lower():
    case "春" | "spring":
        print("春暖花開")
    case "夏" | "summer":
        print("夏日炎炎")
    case "秋" | "autumn" | "fall":
        print("秋高氣爽")
    case "冬" | "winter":
        print("冬風凜冽")
    case _:
        print("輸入錯誤") # 配合迴圈或函式可以讓使用者再次輸入

# -----------------------way 2 -----------------------------------------
while True:
    season = input("請輸入你喜愛的季節: ")
    match season.lower():
        case "春" | "spring":
            print("春暖花開")
            break
        case "夏" | "summer":
            print("夏日炎炎")
            break
        case "秋" | "autumn" | "fall":
            print("秋高氣爽")
            break
        case "冬" | "winter":
            print("冬風凜冽")
            break
        case _:
            print("輸入錯誤，請重新輸入。")


# ------------------------way 3-------------------------------------------------
def ask_season():
    while True:
        season = input("請輸入你喜愛的季節: ")
        match season.lower():
            case "春" | "spring":
                return "春暖花開"
            case "夏" | "summer":
                return "夏日炎炎"
            case "秋" | "autumn" | "fall":
                return "秋高氣爽"
            case "冬" | "winter":
                return "冬風凜冽"
            case _:
                print("輸入錯誤，請重新輸入。")

# 主程式
result = ask_season()
print(result)
