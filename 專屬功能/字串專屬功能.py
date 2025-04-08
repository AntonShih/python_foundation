s = "hello"*5
print(s)

b = s.replace("hello","bye")
print(b)
#有等號設置值才會被取代

s = s.replace("hello","8",2)
print(s)

d = "2023-12-23"
print(d.split("-"))
ds = d.split("-")

dj = "/".join(ds[::-1])
print(dj) #用 / 把清單接成字串

s = " \n abc \t \n"
print(s)
print(s.strip())
#lstrip = 左邊 rstrip = 右邊