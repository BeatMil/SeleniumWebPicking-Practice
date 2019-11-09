from selenium import webdriver
import time
browser_c = webdriver.Chrome()
def freezeQuit():
    input("PRESS ANY KEY ...")
    browser_c.close()

browser_position = {'height': 1020, 'width': 945, 'x' : 947, 'y': 500}
print("BEFORE")
print(browser_c.get_window_rect())
print(type(browser_c.get_window_rect()))

print("AFTER")
browser_c.set_window_rect(947,10,945,1020)
print(browser_c.get_window_rect())
print(type(browser_c.get_window_rect()))


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


# tweets = browser_c.find_elements_by_class_name("css-1dbjc4n r-my5ep6 r-qklmqi r-1adg3ll")
# print("tweets: {}".format(len(tweets)))
        
# Security page 
# asking for phone number
# challenge_responde
try:
    number_slot = browser_c.find_element_by_id("challenge_response")
    number_slot.send_keys("0800765767")
    number_slot.submit()
    
except:
    print("No Security page (phone number)")    

# css-1dbjc4n r-1awozwy r-sdzlij r-18u37iz r-1777fci r-dnmrzs r-1sp51qo r-o7ynqc r-6416eg
browser_c.set_window_size(1600,900)
browser_c.set_window_position(10,10)
time.sleep(1)
more_button = browser_c.find_element_by_xpath("""//*[@id="react-root"]/div/div/div/header/div/div/div/div/div[2]/nav/div/div""")
more_button.click()
time.sleep(1)
browser_c.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[1]/div/div/div[2]/div[3]/div/div/div/div/div[9]/a/div/div[2]/span""").click()
go_back = browser_c.find_element_by_xpath("""//*[@id="react-root"]/div/div/div[1]/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[8]/div/div/div[3]/input""")
go_back.click()
go_back.send_keys(Keys.ESCAPE)
freezeQuit()
