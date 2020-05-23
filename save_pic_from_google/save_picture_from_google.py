# /usr/bin/python3

import os
from selenium import webdriver
keyword = 'nekopara vanilla'
search_engine = 'https://www.google.com/imghp?hl=en'
browser = webdriver.Firefox()
browser.get(search_engine)
#search_box = browser.find_elements_by_tag_name('input')
#print(search_box)
#print(len(search_box))
search_box = browser.find_element_by_name('q')
search_box.send_keys(keyword)
search_box.submit()
#os.system("echo yay")
#os.system("pwd")



