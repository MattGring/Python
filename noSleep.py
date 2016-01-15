#! python3

# noSleep: Clicks the mouse every 240 seconds to keep PC from going to sleep

import pyautogui
import time

sleepTime = 240

print('noSleep.py is running...')
print('Pres Ctrl-C to quit.')

try:
    while True:
        time.sleep(sleepTime)
        pyautogui.click()


except KeyboardInterrupt:
    print('\nDone.')
