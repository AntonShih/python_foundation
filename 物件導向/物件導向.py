#物建導向 : 自訂型態 ->原 python 自訂型態為int,str,list...(小寫)

#我們自訂型態時第一個字應該要大寫
class Person:
    def set_data(self,w,h):
        self.weight = w
        self.height = h

    def calculate_bmi(self,d=2):
        bmi = self.weight / (self.height/100)**2
        return round(bmi,d)
    
# 一個型態可以擁有的兩種東西
# 1.專屬功能 人.吃飯()
# 2.專屬值 人.身高

p1 = Person() #把p1定義成class型態
p1.set_data(80,175) #專屬值
# calculate_bmi(p1) 普通功能轉換成專屬功能
print(p1.calculate_bmi(d=4)) #p1.專屬功能 所以後面不用帶參數 參數即是p1