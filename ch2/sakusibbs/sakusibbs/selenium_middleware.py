from scrapy.http import HtmlResponse
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# Chromeの初期化 --- (※1)
browser_base = \
    "/Users/cedar/.pyenv/versions/anaconda3-2020.02/envs/venv/lib"
browser = browser_base + "/python3.7/site-packages/chromedriver_binary/chromedriver"
driver = Chrome(executable_path=browser)

# Chromeで任意のURLを開く --- (※2)
def selenium_get(url):
  driver.get(url)

# CSSクエリを指定して読込が完了するまで待機 --- (※3)
def get_dom(query):
    dom = WebDriverWait(driver, 10).until(
      EC.presence_of_element_located(
        (By.CSS_SELECTOR, query)))
    return dom

# Chromeを閉じる --- (※4)
def selenium_close():
    driver.close()

# ミドルウェアの本体 --- (※5)
class SeleniumMiddleware(object):
    # リクエストをSeleniumで処理する
    def process_request(self, request, spider):
        driver.get(request.url)
        return HtmlResponse(
                driver.current_url,
                body = driver.page_source,
                encoding = 'utf-8',
                request = request)
