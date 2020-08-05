# In the previous project, the screenshot got saved with the same name i.e. test.png so it replaced the previous screenshot with the new one.
# To avoid this we'll now create variables which will save the screenshot with random numbers
import time
import pyautogui #module which is used to take the screenshot

def Screenshot():
    name = int(round(time.time()*1000)) #it will give the number to the file name
    name = '{}.png'.format(name) #{}- here the number of the file name will be displayed and .png is the extension of the photo
    time.sleep(5) #time before the screenshot | it waits for 5 seconds to take the screenshot
    img = pyautogui.screenshot(name) #saves the screenshot with name as test.png
    img.show() #showing the screenshot taken 

Screenshot()