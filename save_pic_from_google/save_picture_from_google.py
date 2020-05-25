# /usr/bin/python3
"""
I'm trying to use curl command to save pictures from google images
instead of using selenium build-it command
"""

import os
from selenium import webdriver
from time import sleep


keyword = 'nekopara chocola'
search_engine = 'https://www.google.com/imghp?hl=en'  # online search engine
browser = webdriver.Firefox()
browser.get(search_engine)
search_box = browser.find_element_by_name('q')  # get google image search box
search_box.send_keys(keyword)
search_box.submit()
# images page
"""
jsname="Q4LuWd"(before click on image)
class="n3VNCb" (after click on image)
"""
sleep(1)  # wait for page to load then seach for tag 'img'
tag_imgs = browser.find_elements_by_tag_name('img')
print("img_found: ", len(tag_imgs))
count = 0  # number the saved pictures
for i in tag_imgs:
    if i.get_attribute('jsname') == 'Q4LuWd':
        try:
            i.click()
        except Exception as error:
            print("Error: %s" % (error))
        sleep(0.4)
        big_images = browser.find_elements_by_class_name('n3VNCb')
        print("class_n3VBCb found: ", len(big_images))
        for i in big_images:
            source = i.get_attribute('src')
            if source[-3:len(source)] == "jpg":
                # check for last three chars jpg
                os.system('wget -O animu_%s.jpg %s' % (count, source))
            elif source[-3:len(source)] == "png":
                # check for last three chars png
                os.system('wget -O animu_%s.png %s' % (count, source))
            count += 1
