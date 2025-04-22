class Cuboid:
    def __init__(self, length=1.0, width=1.0, height=1.0):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def getInfo(self):
        return f"長: {self.length}, 寬: {self.width}, 高: {self.height}, 體積: {self.volume()}"


def main():
    strList = input("請輸入長方體的長、寬、高(空白間隔): ").split()
    cuboid = Cuboid(float(strList[0]), float(strList[1]), float(strList[2]))
    print("輸入的長方體資訊如下: ")
    print(cuboid.getInfo())


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")

# ----------------------------------------------------------
# class cuboid:
#     def __init__(self,length,width,height):
#         self.length = length
#         self.width = width
#         self.height = height

#     def volume(length,width,height):
#         b = length*width*height
#         return b
#     def getInfo(length,width,height,b):
#         print(getInfo())

# c =[]
# def main():
#     b = input("請輸入長⽅體的長、寬、⾼(空⽩間隔):")
#     c = list(map(int(b).strip()))

#     cuboid1 = cuboid(e,f,g : for i in c:)
#     print(f"輸入的長⽅體資訊如下: /n長:{c[1].2f},寬:{c[2].2f},高:{c[3].2f},體積:{volume.b.2f}")

# ---------------------------------------------------------------------------
class Cuboid:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def getInfo(self):
        print(f"長: {self.length:.1f}",end=", ")
        print(f"寬: {self.width:.1f}",end=", ")
        print(f"高: {self.height:.1f}",end=", ")
        print(f"體積: {self.volume():.1f}",)


def main():
    b = input("請輸入長方體的長、寬、高 (空白間隔): ")
    c = list(map(float, b.strip().split()))
    print(c)
    # 拆出長寬高
    length, width, height = c
    print(length, width, height)
    # 建立物件
    cuboid1 = Cuboid(length, width, height)
    print(cuboid1)

    print("輸入的長方體資訊如下:")
    cuboid1.getInfo()


if __name__ == "__main__":
    main()