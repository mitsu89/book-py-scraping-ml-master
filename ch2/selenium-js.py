from selenium.webdriver import Chrome, ChromeOptions

# Chromeを起動
options = ChromeOptions()
options.add_argument('-headless')
driver_base = \
    "/Users/cedar/.pyenv/versions/anaconda3-2020.02/envs/venv/lib/"
driver = driver_base + "python3.7/site-packages/chromedriver_binary/chromedriver"
browser = Chrome(executable_path=driver, options=options)

# 適当なWebサイトを開く
browser.get("https://google.com")

# JavaScriptを実行
r = browser.execute_script("return 100 + 50")
print(r)
browser.quit()
