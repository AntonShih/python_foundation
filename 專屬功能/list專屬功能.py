scores = [50,40,60]

b = scores.append(99)
print(scores)
print(b)

#破除兩個東西 1.東西絕對不會在等號前面改變 2.到底是原本的list還是新list所以回傳none

print(print(4.2))

#字串 print(s.replace(xxx,ooo))
#這會印出none ,scores.append(888) ->沒有回傳值
#錯誤1 print(scores.append(888))

#字串 s.replace()
# scores = scores.append(777)  #回傳值是none 
#相當於scores = none

scores.append(777)
print(scores)

