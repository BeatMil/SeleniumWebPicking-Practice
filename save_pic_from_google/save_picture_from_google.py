# /usr/bin/python3
"""
I'm trying to use curl command to save pictures from google images
instead of using selenium build-it command
"""
import os
from time import sleep
from selenium import webdriver

keyword = 'nekopara vanilla'
search_engine = 'https://www.google.com/imghp?hl=en'  # online search engine
browser = webdriver.Firefox()
browser.get(search_engine)
search_box = browser.find_element_by_name('q')  # get google image search box
search_box.send_keys(keyword)
search_box.submit()
# images page
# jsname="Q4LuWd"
sleep(1)  # wait for page to load then seach for tag 'img'
tag_imgs = browser.find_elements_by_tag_name('img')
print(len(tag_imgs))
count = 0  # number the saved pictures
for i in tag_imgs:
    if i.get_attribute('jsname') == 'Q4LuWd':
        source = i.get_attribute('src')
        os.system('curl %s > animu_%s' % (source, count))
        count += 1
# os.system("echo yay")
# os.system("pwd")
