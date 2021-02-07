import pyautogui
import time
import win32api
import random
import keyboard
import yaml
from threading import Timer

win32api.SetConsoleTitle('Soldier 76 | Recoil-Control')

def config() :
    with open("settings.yml", 'r', encoding="utf8") as stream :
        try :
            f=yaml.safe_load(stream)
        except yaml.YAMLError as err :
            print(err)
    global horizontal_range
    global min_vertical
    global max_vertical
    global min_firerate
    global max_firerate
    global toggle_button
    horizontal_range = f['horizontal_range']
    min_vertical = f['min_vertical']
    max_vertical = f['max_vertical']
    min_firerate = f['min_firerate']
    max_firerate = f['max_firerate']
    toggle_button = f['toggle_button']
    Timer(1, config).start()
config()

enabled = False
banner = """
<----------------------------------------------------------------->
  ____                _ _        ____            _             _
 |  _ \ ___  ___ ___ (_) |      / ___|___  _ __ | |_ _ __ ___ | |
 | |_) / _ \/ __/ _ \| | |_____| |   / _ \| '_ \| __| '__/ _ \| |
 |  _ <  __/ (_| (_) | | |_____| |__| (_) | | | | |_| | | (_) | |
 |_| \_\___|\___\___/|_|_|      \____\___/|_| |_|\__|_|  \___/|_|

<----------------------------------------------------------------->
"""
# print('<<---- Recoil-Control started! ---->> ')
print(banner)
print('Press '+ toggle_button + ' to enable/disable\n')
if enabled:
    print("Recoil-Control: ENABLED ", end="\r")
else:
    print("Recoil-Control: DISABLED", end="\r")

def is_mouse_down():
    lmb_state = win32api.GetKeyState(0x01)
    return lmb_state < 0

last_state = False
while True:
    key_down = keyboard.is_pressed(toggle_button)
    if key_down != last_state:
        last_state = key_down
        if last_state:
            enabled = not enabled
            if enabled:
                print('Recoil-Control: ENABLED ', end="\r")
            else:
                print('Recoil-Control: DISABLED', end="\r")

    if is_mouse_down() and enabled:
        offset_const = 1000
        horizontal_offset = random.randrange(-horizontal_range * offset_const, horizontal_range * offset_const, 1) / offset_const
        vertical_offset = random.randrange(min_vertical * offset_const, max_vertical * offset_const, 1) / offset_const
        win32api.mouse_event(0x0001, int(horizontal_offset), int(vertical_offset))
        time_offset = random.randrange(min_firerate * offset_const, max_firerate * offset_const, 1) / offset_const
        time.sleep(time_offset)
    time.sleep(0.001)
