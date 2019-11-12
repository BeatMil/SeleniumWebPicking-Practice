from selenium import webdriver 
browser = webdriver.Chrome()
browser.get("http://www.google.com")
print(browser.find_element_by_tag_name("img").get_attribute("src"))


