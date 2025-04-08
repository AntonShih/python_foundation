f = open("a.txt","w",encoding="utf-8")
# 以前寫法 write(f,"abc")
# 專屬功能寫法 : f.wirte("abc")
# 跳脫字元 :\n換行 \t tab
f.write("abc\ndef")
f.write("def")
#以前的寫法: close(f)
# 專屬功能寫法 : fclose()
f.close()

s = open("loop\move.py","r",encoding="utf-8")
#以前 a = 1read(s) 回傳值會是字串
# 專屬功能寫法 : f.read()
a = s.read()
s.close

print(a)