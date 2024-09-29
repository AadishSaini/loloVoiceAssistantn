import pyautogui
import time
print(pyautogui.size())

pyautogui.moveTo(79, 1494)
time.sleep(1)
pyautogui.click()
pyautogui.click() 
time.sleep(1)
pyautogui.moveTo(994, 120)
pyautogui.click()
pyautogui.write('cmd' )
pyautogui.press('enter') 
time.sleep(1)
pyautogui.write('cd ./.venv2' )
pyautogui.press('enter') 
pyautogui.write('cd Scripts' )
pyautogui.press('enter') 
pyautogui.write('activate' )
pyautogui.press('enter')
pyautogui.write('cd ..' )
pyautogui.press('enter')
pyautogui.write('cd ..' )
pyautogui.press('enter')
pyautogui.write('cls' )
pyautogui.press('enter')
pyautogui.write('python main.py' )
pyautogui.press('enter')
# import pyautogui

# while True:
# 	print(pyautogui.position())