#物建導向 : 自訂型態 ->原 python 自訂型態為int,str,list...(小寫)

#我們自訂型態時第一個字應該要大寫
class Person:
    # def __init__(self) #python 內建初始會經過的東西所以我們下面只是重新定義內建的功能
    #     pass

    def __init__(self,w,h):
        self.weight = w
        self.height = h

    def calculate_bmi(self,d=2):
        bmi = self.weight / (self.height/100)**2
        return round(bmi,d)
    
    def __str__(self):
        return "[weight]:{}[height]:{}".format(self.weight,self.height)
    
    def __eq__(self, value):
        return (self.height == value.height) and(self.weight == value.weight)

p1 = Person(80,175) #把p1定義成class型態
print(p1.calculate_bmi(d=4)) #p1.專屬功能 所以後面不用帶參數 參數即是p1

#print(p1) ->先將p1專換成字串 ->str(p1) ->p1.__str__()
print(p1)
p2 = Person(80,175)

#p1 == p2 -> p1.__eq__(p2)
print(p1 == p2)
