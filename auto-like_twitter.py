from selenium import webdriver

browser_c = webdriver.Chrome()
def freezeQuit():
    input("PRESS ANY KEY ...")
    browser_c.close()

browser_c.get("https://twitter.com")
try:
    browser_c.find_element_by_link_text("Log in").click()
except:
    print("(Log in) not found")
try:
    browser_c.find_element_by_link_text("Log In").click()
except:
    print("(Log In) not found")

elems = browser_c.find_elements_by_tag_name("input")

count_loop = 0
for i in range(len(elems)):
    tag_class = elems[i].get_attribute("class")
    print("%d %s" % (i, tag_class))
    if "js-" in tag_class[:3] and count_loop == 0:
        print("----------username slot found.")
        elems[i].send_keys("anutorn@gmail.com")
        count_loop += 1
    elif "js-" in tag_class[:3] and count_loop > 0:
        print("----------password slot found.")
        elems[i].send_keys("Pobo88-7")
        elems[i].submit()
        break
# Twitter each post class: css-1dbjc4n r-my5ep6 r-qklmqi r-1adg3ll


tweets = browser_c.find_elements_by_class_name("css-1dbjc4n r-my5ep6 r-qklmqi r-1adg3ll")
print("tweets: {}".format(len(tweets)))
        
        




freezeQuit()
