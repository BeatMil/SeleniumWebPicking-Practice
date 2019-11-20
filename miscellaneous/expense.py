from selenium import webdriver
from selenium.webdriver.common import keys as ky 
import time
from login_getter import get_login
def freeze_quit():
    input("PRESS ENTER TO EXIT")
    broswer.close()

drive_excel = "http://docs.google.com/spreadsheets/"
user_data = get_login()
email = user_data[0]
password = user_data[1]
broswer = webdriver.Chrome()
broswer.get(drive_excel)
input1 = broswer.find_element_by_tag_name("Input")
input1.send_keys(email)
input1.send_keys(ky.Keys.ENTER)
time.sleep(1)
input2 = broswer.find_elements_by_tag_name("Input")
for i in input2:
    if str(i.get_attribute("type")).count("password"):
        i.send_keys(password)
        i.send_keys(ky.Keys.ENTER)
        break
time.sleep(2)
# Daily expense
tag_div = broswer.find_elements_by_tag_name("div")
for i in tag_div:
    print(i)
    try:
        if i.get_attribute("title").count("Daily expense"):
            i.click()
            break
    except:
        print("if get_attr wrong")



freeze_quit()