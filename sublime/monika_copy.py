#delete monika game
import os
from time import sleep


def get_monika_status(): # check if monika is in the directory
    current_list =  os.listdir() 
    for i in current_list:
        if i.lower() == "monika":
            return True
            break
    return False

count = 0
if not get_monika_status(): #if monika is not here
    f = open("monika","w")
    f.close()
    print("Monika created")
else:
    print("Monika already here")

while get_monika_status():
    sleep(1)
    count += 1
    print("Just monika (%s)"%count)

print("ARRRRRRG")

# print("has_monika: %s"%has_monika)
# print("There is a file name monika.")
# print("Do not delete it")

