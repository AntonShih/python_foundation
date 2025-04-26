class Station:
    def __init__(self, name="", latitude=0.0, longitude=0.0):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return f"站名: {self.name}, 緯度: {self.latitude}, 經度: {self.longitude}"

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)


def main():
    stations = set()
    go = True
    while go:
        name = input("站名: ")
        latitude = float(input("緯度: "))
        longitude = float(input("經度: "))
        station = Station(name, latitude, longitude)
        if station in stations:
            print(f"{station.name}站已經存在")
            continue
        stations.add(station)
        print(station)
        match input("繼續輸入 ( Y | y ): "):
            case "Y" | "y":
                go = True
            case _:
                go = False

    print("車站依照緯度高到低排序如下: ")
    for station in sorted(stations, key=lambda s: s.latitude, reverse=True):
        print(station)


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
# ---------------------------------------------------------------
class station:
    def add_station(self,name="",alt=0.0,long=0.0):
        self.name =  name
        self.alt = alt
        self.long = long

    def show(self):
        print(f"站名:{self.name}/n緯度:{self.alt}/n經度:{self.long}")

def main():
    a=[]
    while True:
        b = input("新增多個⾞站的站名、緯度、經度資料`,空格分開")
    # ------------------------------------------------------------
class Station:
    def __init__(self, name="", lat=0.0, lon=0.0):
        self.name = name
        self.lat = lat
        self.lon = lon

    def show(self):
        print(f"站名: {self.name}\n緯度: {self.lat}\n經度: {self.lon}")


def main():
    stations = []

    while True:
        try:
            # 一次輸入三個值，用空格分開
            data = input("請輸入車站資料 (站名 緯度 經度)，空格分開: ").split()
            if len(data) != 3:
                print("❗ 請輸入正確格式，例如：台中 24.1111 121.1111")
                continue

            name, lat, lon = data[0], float(data[1]), float(data[2])
            s = Station(name, lat, lon)
            stations.append(s)

            cont = input("是否繼續輸入？(y/n): ")
            if cont.lower() != "y":
                break

        except ValueError:
            print("❗ 請輸入正確數字格式的緯度與經度")

    print("\n📍 所有車站資料如下（緯度由高到低）:")
    for s in sorted(stations, key=lambda x: x.lat, reverse=True):
        s.show()
        print("------")


if __name__ == "__main__":
    main()
