from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USER = "JS-TESTER"
PASS = "ipCU12ySxI"

# Chromeのドライバを得る --- (※1)
options = ChromeOptions()
options.add_argument('-headless')
driver_base = \
    "/Users/cedar/.pyenv/versions/anaconda3-2020.02/envs/venv/lib/"
driver = driver_base +  "python3.7/site-packages/chromedriver_binary/chromedriver"
browser = Chrome(executable_path=driver, options=options)

# ログインページにアクセス --- (※2)
url_login = "https://uta.pw/sakusibbs/users.php?action=login"
browser.get(url_login)
print("ログインページにアクセスしました")

# テキストボックスに文字を入力 --- (※3)
e = browser.find_element_by_id("user")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pass")
e.clear()
e.send_keys(PASS)
# フォームを送信 --- (※4)
frm = browser.find_element_by_css_selector("#loginForm form")
frm.submit()
print("情報を入力してログインボタンを押しました")
# ページのロード完了まで待機 --- (※5)
WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".islogin")))

# マイページのURLを得る --- (※6)
a = browser.find_element_by_css_selector(".islogin a")
url_mypage = a.get_attribute('href')
print("マイページのURL=", url_mypage)

# マイページを表示 --- (※7)
browser.get(url_mypage)

# お気に入りのタイトルを列挙 --- (※8)
links = browser.find_elements_by_css_selector(
    "#favlist li > a")
for a in links:
    href = a.get_attribute('href')
    title = a.text
    print("-", title, ">", href)

browser.quit()
