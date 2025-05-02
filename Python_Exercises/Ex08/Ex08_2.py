# class CubeError(BaseException):
#     def __init__(self, message):
#         self.message = message

#     def __str__(self):
#         return f"CubeError: {self.message}"


# class Cube:
#     def __init__(self, length):
#         self.__length = 0.0
#         self.length = length

#     @property
#     def length(self):
#         return self.__length

#     @length.setter
#     def length(self, length):
#         if length <= 0.0:
#             raise CubeError(f"正立方體邊長不可為0或負數")
#         else:
#             self.__length = length

#     def volume(self):
#         return self.length ** 3

#     def __str__(self):
#         return f"邊長: {self.length}, 體積: {self.volume()}"


# def main():
#     while True:
#         try:
#             length = float(input("立方體邊長: "))
#             cube = Cube(length)
#             print(cube)
#             break
#         except ValueError:
#             print("數字格式不正確，請重新輸入")
#         except CubeError as err:
#             print(f"{err}，請重新輸入")


# if __name__ == "__main__":
#     print("===================================")
# 
# ------------------------------------------------------------
# 定義自訂錯誤類別 CubeError，繼承 BaseException
class CubeError(BaseException):
    def __init__(self, message):
        self.message = message  # 儲存錯誤訊息

    def __str__(self):
        return f"CubeError: {self.message}"  # 定義當錯誤被印出時的格式


# 定義 Cube 類別，代表一個正立方體
class Cube:
    def __init__(self, length):
        self.__length = 0.0    # 先設定私有屬性 __length 為 0.0
        self.length = length   # 再用 setter 方法設定正確的邊長（會自動做防呆檢查）

    @property
    def length(self):
        return self.__length  # 讀取私有屬性 __length

    @length.setter
    def length(self, length):
        # 設定邊長時，先檢查新傳入的 length 是否合理
        if length <= 0.0:
            raise CubeError(f"正立方體邊長不可為0或負數")  # 拋出自訂錯誤
        else:
            self.__length = length  # 合法的話才設定到私有變數

    def volume(self):
        # 計算體積（邊長的三次方）
        return self.length ** 3

    def __str__(self):
        # 定義當 Cube 物件被印出時，顯示邊長與體積
        return f"邊長: {self.length}, 體積: {self.volume()}"


# 主程式入口

def main():
    while True:
        try:
            # 請使用者輸入邊長，並轉成 float
            length = float(input("立方體邊長: "))
            cube = Cube(length)  # 建立 Cube 物件（會觸發驗證）
            print(cube)          # 印出邊長和體積
            break  # 成功建立後就跳出 while 迴圈

        except ValueError:
            # 如果輸入無法轉成數字（例如輸入"abc"），捕捉錯誤
            print("數字格式不正確，請重新輸入")

        except CubeError as err:
            # 如果邊長為0或負數，捕捉自訂錯誤，並印出錯誤訊息
            print(f"{err}，請重新輸入")


# 程式執行入口，確保只有直接執行此檔案時才會跑 main
if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")