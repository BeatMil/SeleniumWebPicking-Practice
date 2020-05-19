import keyboard as kb
import time 

kb.press_and_release("win+d")
kb.send('windows')
time.sleep(0.1)
kb.write("notepad")
time.sleep(0.1)
kb.send("enter")
