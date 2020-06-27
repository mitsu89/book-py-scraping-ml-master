from bs4 import BeautifulSoup
import urllib.request as req

# 為替情報XMLを取得
url = "https://api.aoikujira.com/index.php?fx"
# url = "https://api.aoikujira.com/kawase/ratecalc.html"  # xml/usd"
res = req.urlopen(url)

# HTMLを解析
soup = BeautifulSoup(res, "html.parser")
print(soup)
# 任意のデータを抽出 --- (※1)
# jpy = soup.select_one("jpy").string
# print("usd/jpy=", jpy.string)
# jpy_list = soup.select("input#f_rate > value")
jpy_list = soup.select("input#f_rate")
print(jpy_list)
for jpy in jpy_list:
    print("usd/jpy=", jpy["value"])