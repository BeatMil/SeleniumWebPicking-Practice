from selenium import webdriver
from time import sleep

google_signin_link = "https://accounts.google.com/signin/v2/identifier?" + \
        "passive=1209600&continue=https%3A%2F%2Fphotos.google.com%2F" + \
        "login&followup=https%3A%2F%2Fphotos.google.com%2Flogin&flowName" + \
        "=GlifWebSignIn&flowEntry=ServiceLogin"
gmail = "anutorn@gmail.com"
password = "bob214*JIN*"
browser = webdriver.Firefox()
browser.get(google_signin_link)
browser.find_element_by_name("identifier").send_keys(gmail)
browser.find_element_by_class_name("CwaK9").click()  # hit submit
sleep(2)
browser.find_element_by_name("password").send_keys(password)
browser.find_element_by_class_name("CwaK9").click()
# we logged in!
browser.find_element_by_xpath("""/html/body/div[1]/div/c-wiz/c-wiz/div/div[1]/div[2]/div[2]/div/div[2]/div/div[2]""").click()
sleep(1)
# css selector is the best!
button = browser.find_element_by_css_selector("div.JPdR6b:nth-child(17) > div:nth-child(1) > div:nth-child(1) > span:nth-child(2) > div:nth-child(3) > div:nth-child(1)")
button.click()
# ActionChains(browser).click(button).perform()

# span_tags = browser.find_elements_by_tag_name("span")
# print(len(span_tags))
# for i in span_tags:
#     if i.get_attribute('class') == "z80M1 o7Osof":
#         i.execute_script("arguments[0].scrollIntoView(true)", i)
#         i.click()
