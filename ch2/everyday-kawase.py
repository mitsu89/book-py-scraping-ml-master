from bs4 import BeautifulSoup
import urllib.request as req
import datetime
import json


# Web APIにアクセス
# API = "https://api.aoikujira.com/kawase/get.php?code=USD&format=json"
# json_str = request.urlopen(API).read().decode("utf-8")
# data = json.loads(json_str)
# print("1USD="+data["JPY"]+"JPY")
'''
現在　Web APIは提供を中止しているので、ch1のbs-kawase.pyと同様の方法で
1USD=JPY を求め、json dumpしたものを　json load
'''
url = "https://api.aoikujira.com/index.php?fx"
res = req.urlopen(url)
# HTMLを解析
soup = BeautifulSoup(res, "html.parser")
jpy_list = soup.select("input#f_rate")
for jpy in jpy_list:
    jpy_value = float(jpy["value"])

kawase_dic = {}
kawase_dic.setdefault('JPY', jpy_value)
data_json = json.dumps(kawase_dic)
data = json.loads(data_json)
print("1USD="+str(data["JPY"])+"JPY")

# 保存ファイル名を決定
t = datetime.date.today()
fname = t.strftime("%Y-%m-%d") + ".json"
with open(fname, "w", encoding="utf-8") as f:
    f.write(data_json)
