import time
import pyautogui #module which is used to take the screenshot

def Screenshot():
    time.sleep(5) #time before the screenshot | it waits for 5 seconds to take the screenshot
    img = pyautogui.screenshot('test.png') #saves the screenshot with name as test.png
    img.show() #showing the screenshot taken 

Screenshot()