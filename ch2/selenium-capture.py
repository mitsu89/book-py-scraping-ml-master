from selenium.webdriver import Chrome, ChromeOptions

url = "https://www.aozora.gr.jp/cards/000081/files/46268_23911.html"

# Chromeをヘッドレスモードを有効にする --- (※1)
options = ChromeOptions()
options.add_argument('-headless')
driver_base = \
    "/Users/cedar/.pyenv/versions/anaconda3-2020.02/envs/venv/lib"
driver = driver_base + "/python3.7/site-packages/chromedriver_binary/chromedriver"

# Chromeを起動する --- (※2)
browser = Chrome(executable_path=driver, options=options)

# URLを読み込む --- (※3)
browser.get(url)

# 画面をキャプチャしてファイルに保存 --- (※4)
browser.save_screenshot("website.png")
# ブラウザを終了 --- (※5)
browser.quit()
