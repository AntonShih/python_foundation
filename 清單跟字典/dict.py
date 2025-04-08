person = {
    "name":"anton",
    "height":175
}
print(person)
#名稱 ->字典[key]
#print(height)
print(person["height"])

#weight = 80
person["weight"] = 80
print(person)

#height = height+5
person["height"] = person["height"]+5
print(person)

#好用的刪除
del person["name"]
print(person)