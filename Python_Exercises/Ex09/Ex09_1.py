from pathlib import Path


def userInput():
    lines = ""
    print("輸入資料 (或直接按 Enter 結束): ")
    while True:
        line = input()
        # 空字串被視為False
        if line:
            lines += line + "\n"
        else:
            break

    return lines


def demoWrite(filePath, text):
    # "a" (append) 代表在已有的檔案內容附加文字
    with filePath.open(mode="w", encoding="UTF-8") as f:
        f.write(text + "\n")
    print("存檔完畢!")


def main():
    writeDir = Path("Python_Exercises\Ex09", "write")
    # 存放目錄不存在就建立，相對路徑代表存放位置跟執行的Python檔案放在同一目錄
    writeDir.mkdir(exist_ok=True)

    writeFile = writeDir/"memo.txt"
    demoWrite(writeFile, userInput())


if __name__ == "__main__":
    print("===================================")
    main()
    print("===================================")
