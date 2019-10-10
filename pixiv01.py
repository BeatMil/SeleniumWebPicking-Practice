from selenium import webdriver

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

browser.get("https://www.pixiv.net")
elem = browser.find_element_by_link_text("Login")
print(elem.text) # YASS It works!!


freezeQuit()
browser.quit()
