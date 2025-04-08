import urllib.request as req
import json

url = ""
f = req.urlopen(url)
s = f.read() #先讀取成bite型態(bite等於圖檔)
print(type(s))
#--------------------------------------------------------------
pics = json.loads(s) #在轉換成轉換城list型態 文字、圖檔
print(type(pics))

#-------------------------------------------------------
pics = json.load(f) #.read 幫你讀取並且轉換成為list及字典

for p in pics: #p是字典
    print(type(p))
    print(p["title"])
    img = "http: +p[high_res_url]"
    print(img)
    print("-" * 30)