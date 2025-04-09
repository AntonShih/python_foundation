weight = 80
height = 175

#定義參數 :預先定義一個參數代號/名稱
#定義回傳值 : return ，你沒有寫return就相當於你寫return none
def calculate_BMI(w,h,d=2):
    bmi = w/(h/100) **2
    return round(bmi,d)

print(calculate_BMI(weight,height))
