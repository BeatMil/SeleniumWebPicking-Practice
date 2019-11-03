from selenium import webdriver
from urllib import request
import sys
import time
from eventlet.timeout import Timeout
def freezeQuit():
    user_choice = input('Please click ENTER button to close application')
    if not user_choice:
        print ("ABORTED")
        browser.close()
    else: 
        print("don't type!!")
        browser.close()

def sleep(seconds):
    print("sleeping for %d" % seconds)
    time.sleep(seconds)


animu_grill_name = input("Insert animu name: ") 
# Google.com
browser = webdriver.Chrome()
browser.get("https://google.com")
search_box = browser.find_element_by_name("q")
# Search for the waifu
search_box.send_keys(animu_grill_name)
search_box.submit()
# Go to images
browser.find_element_by_link_text("Images").click()
"""
Open new tab with specific link!

fish_web = "http://www.youtube.com"

browser.execute_script('''window.open("%s","_blank");''' % fish_web)

"""
#############################################################################################
# anime section
# imgs = browser.find_elements_by_tag_name("img")

# # TOP SECRET !! class = "irc_mi"
# alt:  Image result for hibiki kancolle

"""
print("imgs type: %s" % type(imgs))

print(("id: "), imgs[index].get_attribute("id"))
print(("href: "), imgs[index].get_attribute("href"))
"""
# scroll down and wait then scroll again
browser.execute_script("window.scrollTo(0, 40000)") 
sleep(1)
browser.execute_script("window.scrollTo(0, 40000)") 

imgs = browser.find_elements_by_tag_name("img")
src_amount = len(imgs)
print("Amount of links: %d" % src_amount)

# index = 30
# print(("src: "), imgs[index].get_attribute("src"))
# print(("alt: "), imgs[index].get_attribute("alt"))
# if imgs[index].get_attribute("alt") == "Image result for hibiki kancolle":
#         imgs[index].click()
# else:
#     print("not hibiki")

big_images = []
for i in range(len(imgs)):
    print("i: %s" % i)
    # print things defensively
    try:
        # print(("src: "), imgs[i].get_attribute("src"))
        print(("alt: "), imgs[i].get_attribute("alt"))
    except:
        print("---get_attribute error---")
    try:
        if imgs[i].get_attribute("alt") == "Image result for %s" % (animu_grill_name):
            try:
                imgs[i].click()
                big_images = browser.find_elements_by_class_name("irc_mi")
                print("big_images range: %s" % len(big_images))
            except:
                print("---elem not clickable.---")
        else:
            print("not $s no click" % animu_grill_name)
    except:
        print("---Error in if statement---")
    if big_images and i%3 == 0:
        for i2 in range(len(big_images)):
            src = big_images[i2].get_attribute("src")
            # print("src: %s" % src)
            if src:
                print("requesting!!!")
                try:
                    timeout = Timeout(0.2, False)
                    request.urlretrieve(src,("%s%s_%s.png" % (animu_grill_name, i, i2)))
                except:
                    print("---HTML Error---")
                    # print("!!!!TIMEOUT!!!!")
    






# for i in range(src_amount):
#     src = imgs[i].get_attribute("src")
#     print("src: %s" % src)

#     if src:
#         print("%d: downloaded" % i)
#         request.urlretrieve(src,"hibiki%d.png" % i)
#     else:
#         print("%d: no download" % i)

freezeQuit()
