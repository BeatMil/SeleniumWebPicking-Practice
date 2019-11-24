from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--mute-audio")
browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get("https://www.youtube.com/watch?v=aRYiLarZPKc")
while True:
    # try:
    #     mute = browser.find_element_by_id("ytd-player")
    #     if mute:
    #         print("FOUND")
    #         mute.send_keys("m")
    # except:
    #     print("NOT FOUND")
    time.sleep(2)
    browser.refresh()
    