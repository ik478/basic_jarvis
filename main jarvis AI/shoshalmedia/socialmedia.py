from  time import sleep
import pyautogui
from Body.Listen import MicExecution
from Body.Speak import Speak
import re
import os

def send_message(Data):
    print(Data)
    pattern ="send a message to (\D*)"
    matchs = re.findall(pattern,Data)
    print(matchs)
    Speak("what's the messege sir")
    Data1 = MicExecution()
    message = Data1
    os.startfile("C:/Program Files/Google/Chrome/Application/chrome_proxy.exe")
    sleep(2)
    pyautogui.write("https://web.whatsapp.com")
    sleep(1)
    pyautogui.press('enter')
    sleep(25)
    pyautogui.hotkey('ctrl','Alt','/')
    sleep(3)
    pyautogui.write(matchs)
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.write(message)
    sleep(1)
    pyautogui.press('enter')
    return "messege was sent sir"
