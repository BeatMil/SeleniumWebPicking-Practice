from selenium import webdriver

browser = webdriver.Chrome()

def freezeStop():
    input("THIS IS THE END OF THE PROGRAM")
    browser.close()
    pass

browser.get("http://www.twitter.com")
browser.find_element_by_link_text("Log In").click()

freezeStop()
