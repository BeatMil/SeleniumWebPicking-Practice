from selenium import webdriver

# driver_firefox = webdriver.Firefox()
browser = webdriver.Firefox()
# driver_firefox.get("https://google.com")
browser.get("https://youtube.com")

# This works too!
# driver_firefox.get("https://www.google.com")
# driver_firefox2.find_element_by_link_text('Sign in')
sign_in_button = browser.find_element_by_css_selector("ytd-button-renderer")
print(sign_in_button)
sign_in_button.click()
