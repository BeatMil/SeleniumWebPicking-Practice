from selenium import webdriver
from urllib import request

def freezeQuit():
    user_choice = input('Please click ENTER button to close application')
    if not user_choice:
        print ("ABORTED")
        browser.close()
    else: 
        print("don't type!!")
        browser.close()


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
# img = browser.find_element_by_xpath("""//*[@id="USkkXF79ja6nJM:"]""")
# src = img.get_attribute('src')

# request.urlretrieve(src, "hibiki.png")
imgs = browser.find_elements_by_tag_name("img")

# for img in imgs:
#     i = 1
#     src = img.get_attribute('src')
#     print(src,"\n")
#     request.urlretrieve(src, "hibiki.png")
#     i += 1

src_amount = len(imgs)
print("Amount of links: %d" % src_amount)

print("imgs type: %s" % type(imgs))

for i in range(src_amount):
    src = imgs[i].get_attribute("src")
    print("src: %s" % src)

    if src:
        print("%d: downloaded" % i)
        request.urlretrieve(src,"hibiki%d.png" % i)
    else:
        print("%d: no download" % i)

freezeQuit()
