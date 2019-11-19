from selenium import webdriver
from selenium.webdriver.common import keys as ky 
import time
def freeze_quit():
    input("PRESS ENTER TO EXIT")
    broswer.close()

drive_excel = "http://docs.google.com/spreadsheets/"
email = ""
password = ""
broswer = webdriver.Chrome()
broswer.get(drive_excel)
input1 = broswer.find_element_by_tag_name("Input")
input1.send_keys(email)
input1.send_keys(ky.Keys.ENTER)
time.sleep(1)
input2 = broswer.find_element_by_tag_name("Input").get_attribute("type")
input2.send_keys(password)
input2.send_keys(ky.Keys.ENTER)




freeze_quit()