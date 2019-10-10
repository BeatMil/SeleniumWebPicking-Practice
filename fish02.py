from selenium import webdriver

youtube_link = 'https://youtube.com'
selenium_link = 'https://www.seleniumhq.org'
reg_link = 'https://reg.stamford.edu'

def freezeQuit():
    user_choice = input('Please click ENTER button to close application')
    if not user_choice:
        print ("ABORTED")
        quit()
    else: 
        print("don't type!!")
        quit()


browser = webdriver.Chrome()
# reg.stamford.edu PAGE
browser.get(reg_link)
elem = browser.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[1]/table/tbody/tr[4]/td/a")
print(elem.get_attribute('href'))
elem.click()

# Login PAGE
print("Type of elem: ", type(elem))

username_slot = browser.find_element_by_name("f_uid")
password_slot = browser.find_element_by_name("f_pwd")
print(username_slot.get_attribute("size"))

username_slot.send_keys("1803020022")
password_slot.send_keys("Pobo88-7")
password_slot.submit()

# Change password PAGE
back_button = browser.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[1]/table/tbody/tr[3]/td/a")
back_button.click()

# Main PAGE
try:
    browser.find_element_by_class_name('AAA')
except:
    print("Error AAA class not found.")








freezeQuit()







# elem = browser.find_element_by_link_text('Download')
# elem.click()
