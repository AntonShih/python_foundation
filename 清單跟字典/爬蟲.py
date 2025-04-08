# import urllib.request as req
# import json
import os
import sys

# url = ""
# f = req.urlopen(url)
# s = f.read() #先讀取成bite型態(bite等於圖檔)
# print(type(s))
# #--------------------------------------------------------------
# pics = json.loads(s) #在轉換成轉換城list型態 文字、圖檔
# print(type(pics))

# #-------------------------------------------------------
# pics = json.load(f) #.read 幫你讀取並且轉換成為list及字典

# for p in pics: #p是字典
#     print(type(p))
#     print(p["title"])
#     img = "http: +p[high_res_url]"
#     print(img)
#     #urlretrieve(圖片網址，處存檔案路徑)
#     print("-" * 30)

dirname = "google"
#如果資料夾不存在，就創造起來
if not os.path.exists(dirname):
    os.makedirs(dirname)

# #字串的專屬功能 list
# # a = "2023-12-31".split("-")
# a = "2023-12-31"
# print(a) 
# print(a[-1])

# fp = dirname + "/"+a.split("-")[-1]

