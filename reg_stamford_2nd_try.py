from selenium import webdriver

def freeze_quit():
    if input("Enter to quit"):
        print("""DON'T TYPE!!!""")
    browser.close()

reg_link = "https://reg.stamford.edu"
browser = webdriver.Chrome()
browser.get(reg_link)
imgs = browser.find_elements_by_tag_name("img")
for i in imgs:
    src = i.get_attribute("src")
    if str(src).count("login"):
        i.click()
        break

f = open("pass.txt", "r")
user_data = f.readlines()
le = len(user_data)
for i in range(le):
    if i < le - 1:
        user_data[i] = user_data[i][:-1]
username = user_data[0]
password = user_data[1]
# username slot tag input attr name="f_uid"
# password slot tag input attr name="f_pwd"
input_tag_elems = browser.find_elements_by_tag_name("input")
print(len(input_tag_elems))
for i in input_tag_elems:
    print(i.get_attribute("name"))
    if i.get_attribute("name") == "f_uid":
        i.send_keys(username)
    elif i.get_attribute("name") == "f_pwd":
        i.send_keys(password)
        i.submit()
        break
# change password page
# imgs = browser.find_elements_by_tag_name("img")
browser.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[1]/table/tbody/tr[3]/td/a").click()

# Menu page
tag_imgs = browser.find_elements_by_tag_name("img")
for img in tag_imgs:
    src = img.get_attribute("src")
    if str(src).count("adddrop"):
        img.click()
        break
# Almost at enroll page
browser.find_element_by_xpath("/html/body/table/tbody/tr[1]/td[3]/table/tbody/tr[4]/td[2]/form/input").click()

freeze_quit()
