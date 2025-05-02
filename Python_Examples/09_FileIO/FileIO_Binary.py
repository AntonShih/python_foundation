from pathlib import Path

# 同時讀寫檔案資料
def demoReadWriteBinary(source, destination):
    print(f"source: {source}")
    print(f"destination: {destination}")
    # 怕檔案過大建議設定讀入並暫存的資料量(byte)
    chunk_size = 1024
    with source.open(mode="rb") as fs, destination.open(mode="wb") as fd:
        while True:
            chunk = fs.read(chunk_size)
            # 讀到檔尾會回傳空字串，空字串被視為False，所以"not chunk"成立就代表資料已經讀完
            if not chunk:
                break
            print(f"讀到 {len(chunk)} bytes")   # 👈 每次讀多少bytes就印出來看
            # 將暫存資料寫入目的檔案
            fd.write(chunk)
            chunk = fs.read(chunk_size)


def main():
    readDir = Path("Python_Examples/09_FileIO", "read")
    writeDir = Path("Python_Examples/09_FileIO", "write")
    # 存放目錄不存在就建立，相對路徑代表存放位置跟執行的Python檔案放在同一目錄
    writeDir.mkdir(exist_ok=True)

    demoReadWriteBinary(readDir/"image.png", writeDir/"binary.png")


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")