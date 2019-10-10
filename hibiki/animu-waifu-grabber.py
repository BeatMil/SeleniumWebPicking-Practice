from selenium import webdriver
from urllib import request

animu_grill_name = "hibiki kancolle"
# Google.com
browser = webdriver.Chrome()
browser.get("https://google.com")
search_box = browser.find_element_by_name("q")
# Search for the waifu
search_box.send_keys(animu_grill_name)
search_box.submit()
# Go to images
browser.find_element_by_link_text("Images").click()
# Save the first pic
img = browser.find_element_by_xpath("""//*[@id="USkkXF79ja6nJM:"]""")
src = img.get_attribute('src')

request.urlretrieve(src, "hibiki.png")
