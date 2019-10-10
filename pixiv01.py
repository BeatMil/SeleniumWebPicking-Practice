from selenium import webdriver
import time
username = 'anutorn'
password = 'Pobo88-7'


def freezeQuit():
    user_choice = input('Please click ENTER button to close application')
    if not user_choice:
        print ("ABORTED")
    else: 
        print("don't type!!")

browser = webdriver.Chrome()

## It worked!!! Command about readjusting window size and position
# print(browser.get_window_position())

# browser.set_window_position(5,5)
# print(browser.get_window_position())

# print(browser.get_window_rect())
# browser.set_window_rect(100,100,800,800)
# print(browser.get_window_rect())


# Front page PIXIV
browser.get("https://www.pixiv.net")
elem = browser.find_element_by_link_text("Login")
print(elem.text) # YASS It works!!
elem.click()

# Login page PIXIV
login_field = browser.find_element_by_xpath("""//*[@id="LoginComponent"]/form/div[1]/div[1]/input""")
password_field = browser.find_element_by_xpath("""//*[@id="LoginComponent"]/form/div[1]/div[2]/input""")

login_field.send_keys(username)
password_field.send_keys(password)
password_field.submit()
#reCapcha pop up
print("sleeping...")
time.sleep(3)
print("slept for 3 second")
# browser.find_element_by_class_name("recaptcha-checkbox-border").click()

"""
This is a comment?
so I can't get past reCapcha.
It too stonk.
"""



freezeQuit()
browser.quit()
