import os
from time import sleep
count = 0
def get_monika_status():
    for i in os.listdir():
        if i.lower() == "monika":
            return True
    else:
        return False
def press_enter():
    input("PRESS ENTER")

if not get_monika_status():
    file = open("monika","w")
    file.close()
    print("Monika created")
else:
    print("Monika here")

while get_monika_status():
    sleep(1)
    count += 1
    print('Just Monika (%s)'%count)

print("ARGGGG")