from selenium import webdriver
import time

browser = webdriver.Chrome()

browser.get("https://www.google.com")
time.sleep(2)
browser.close()
print("Program Done")