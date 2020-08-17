from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument("window-size=1400,600")
from fake_useragent import UserAgent
ua = UserAgent()
a = ua.random
user_agent = ua.random
print(user_agent)
options.add_argument(f'user-agent={user_agent}')
driver = webdriver.Chrome(chrome_options=options,executable_path = "/usr/lib/chromium-browser/chromedriver")
driver.get('https://whoer.net/')
