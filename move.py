# s = "hello"
# s[0] = "h"
# s[1] = "e"
#在python算長度都是用len(s) = 5

x , y = 0 , 0
# x = -2 y = 0
commands = "ULLRDL"
i = 0 
while i < len(commands):
    c = commands[i]
    print(c)
    if c == "U": #相等永遠是 ==
        y = y + 1
    elif c == "D": #相等永遠是 ==
        y = y - 1
    elif c == "R": #相等永遠是 ==
        x = x + 1
    elif c == "L": #相等永遠是 ==
        x = x - 1
    i = i + 1
print(x,y)