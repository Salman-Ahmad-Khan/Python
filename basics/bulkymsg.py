import pyautogui
import time
time.sleep(5)
count=0

while count<=100:
    pyautogui.typewrite("hello.🤏😎")
    pyautogui.press("enter")
    count=count+1