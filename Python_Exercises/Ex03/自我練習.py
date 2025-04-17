# # #  題目：飲料點單小助手（使用 match-case）
# # 請設計一個小程式，讓使用者輸入想喝的飲料名稱（例如：紅茶、綠茶、奶茶、美式、拿鐵），
# # 程式會根據輸入顯示不同回覆，例如顯示價錢或推薦話語。
# # 如果輸入的飲料不在選單內，要顯示「無此品項，請重新輸入」。

# # 請輸入你要的飲料：奶茶
# # 奶茶：香濃滑順，一杯 50 元！

# # 請輸入你要的飲料：咖啡
# # 無此品項，請重新輸入。

# # 使用 match-case 判斷輸入的飲料

# # 支援大小寫不敏感（建議用 .lower()）

# # 飲料選項（可用）：紅茶、綠茶、奶茶、美式、拿鐵

# # 每個選項至少給出一句不同的回覆

# # 可以用 while 讓使用者輸錯可重新輸入（進階加分）



# while True:
#     drinks = input("請輸入想喝的飲料（例如：紅茶、綠茶、奶茶、美式、拿鐵）: ").strip().lower()
#     match drinks:
#         case "紅茶" | "blacktea":
#             print("紅茶售價: 20 元")
#             break
#         case "綠茶" | "greentea":
#             print("綠茶售價: 5 元")
#             break
#         case "奶茶" | "milktea":
#             print("香濃滑順，一杯 50 元！")
#             break
#         case "美式" | "americano":
#             print("美式售價: 70 元")
#             break
#         case "拿鐵" | "latte":
#             print("拿鐵售價: 75 元")
#             break
#         case _:
#             print("無此品項，請重新輸入。")
# ----------------------------------------------------------------
total = 0  # 總金額

print("💁 歡迎光臨！請輸入想喝的飲料，輸入 q 可以結束點餐。\n")

while True:
    drinks = input("請輸入飲料（紅茶、綠茶、奶茶、美式、拿鐵）：").strip().lower()

    if drinks == "q":
        break

    match drinks:
        case "紅茶" | "blacktea":
            print("✔️ 紅茶售價：20元")
            total += 20
        case "綠茶" | "greentea":
            print("✔️ 綠茶售價：25元")
            total += 25
        case "奶茶" | "milktea":
            print("✔️ 奶茶售價：50元")
            total += 50
        case "美式" | "americano":
            print("✔️ 美式售價：70元")
            total += 70
        case "拿鐵" | "latte":
            print("✔️ 拿鐵售價：75元")
            total += 75
        case _:
            print("❌ 無此品項，請重新輸入。")

print(f"\n🧾 您的總金額為：{total} 元")
print("🙏 謝謝光臨！")
