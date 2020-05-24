from selenium import webdriver
from time import sleep


# class = "p-row js-link "
my_csgostat_site = "https://csgostats.gg/player/76561197990906124#/matches"
browser = webdriver.Chrome()
browser.get(my_csgostat_site)
sleep(3)
csgo_match_rows = browser.find_elements_by_tag_name("tr")
print(len(csgo_match_rows))

for i in csgo_match_rows:
    try:
        i.click()
    except Exception as e:
        print(e)

if input("PRESS ANY KEY"): # press key before quit
    exit()
