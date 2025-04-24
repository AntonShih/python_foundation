class Cuboid:
    def __init__(self, length=1.0, width=1.0, height=1.0):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def getInfo(self):
        return f"長: {self.length}, 寬: {self.width}, 高: {self.height}, 體積: {self.volume()}"

    @staticmethod
    def getCuboidsInfo(cuboids):
        text = ""
        for cuboid in cuboids:
            text += cuboid.getInfo() + "\n"

        return text


def inputCuboids(num):
    cuboids = []
    for i in range(num):
        length, width, height = list(
            map(float, input(f"請輸入第{i + 1}個長方體的長、寬、高(空白間隔): ").split()))
        cuboid = Cuboid(length, width, height)
        cuboids.append(cuboid)

    return cuboids


def main():
    num = int(input("請問有幾個長方體? "))
    cuboids = inputCuboids(num)
    print(f"輸入的{num}個長方體資訊如下:")
    print(Cuboid.getCuboidsInfo(cuboids))


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
# #----------------------------------------------------------------





# def main():
#     a = int(input("請問有幾個長⽅體?"))
#     for i in range(1,a+1):
#         b = input(f"請輸入第{i}個長⽅體的長、寬、⾼(空⽩間隔):")
#         c = list(map(int,b.strip()))
#         print(f"輸入的{a}個長方形資訊如下: /n長:{c[0]:.1f},  寬: {c[1]:.1f}, ⾼:{c[2]:.1f}, 體積: 1.0" )

# if __name__ == "__main__":
#     print("===================================")
#     main()
#     print("===================================")
#----------------------------------------------------
####基本寫法
# def main():
#     a = int(input("請問有幾個長方體? "))
    
#     print(f"\n輸入的 {a} 個長方體資訊如下：")
    
#     for i in range(1, a + 1):
#         b = input(f"請輸入第 {i} 個長方體的長、寬、高（空白間隔）：")
#         c = list(map(float, b.strip().split()))  # 修正這裡：要 split 才會切成 list

#         length, width, height = c
#         volume = length * width * height

#         print(f"長: {length:.1f}, 寬: {width:.1f}, 高: {height:.1f}, 體積: {volume:.1f}")

# if __name__ == "__main__":
#     print("===================================")
#     main()
#     print("===================================")

#-----------------------------------------------------------------------------------------------
class Cuboid:
    def __init__(self, length=1.0, width=1.0, height=1.0):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def getInfo(self):
        return f"長: {self.length}, 寬: {self.width}, 高: {self.height}, 體積: {self.volume()}"

    def __str__(self):
        # print(cuboid) 時會呼叫這個
        return self.getInfo()

    def __repr__(self):
        # print(cuboids)（list）或直接輸出物件時會呼叫這個
        return f"Cuboid({self.length}, {self.width}, {self.height})"

    @staticmethod
    def getCuboidsInfo(cuboids):
        return "\n".join(map(str, cuboids))
 
def main():
    print("歡迎使用長方體系統")
    num = int(input("請問你要輸入幾個長方體？"))
    
    cuboids = inputCuboids(num)

    print("\n▶ 所有長方體資訊如下：")
    for c in cuboids:
        print(c)  # 呼叫 __str__()

    print("\n▶ 體積 > 100 的長方體：")
    largeCuboids = list(filter(lambda c: c.volume() > 100, cuboids))
    if largeCuboids:
        for c in largeCuboids:
            print(c)
    else:
        print("沒有體積超過 100 的長方體")

    print("\n▶ 體積最大的長方體：")
    maxCuboid = max(cuboids, key=lambda c: c.volume())
    print(maxCuboid)

    print("\n▶ 按體積由小到大排序：")
    sortedCuboids = sorted(cuboids, key=lambda c: c.volume())
    for c in sortedCuboids:
        print(c)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")