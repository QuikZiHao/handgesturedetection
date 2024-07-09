import pyautogui
import time
import os
from datetime import datetime
from utils.checkOS import detect_os

def do_copy():
    time.sleep(1)
    pyautogui.hotkey('ctrl','c')


def do_paste():
    time.sleep(1)
    pyautogui.hotkey('ctrl','v')


def do_screenshot():
    screenshot = pyautogui.screenshot()
    file_path = os.path.join('assets',datetime.now().strftime("%Y%m%d%H%M%S.png"))
    screenshot.save(file_path)
    
    
def next_track():
    def windows_action():
    # Simulate pressing the 'Next Track' multimedia key
        pyautogui.press('nexttrack')

    def macos_action():
    # Simulate pressing Control + Command + Right Arrow
        pyautogui.hotkey('ctrl', 'command', 'right')

    def linux_action():
    # Simulate pressing Alt + Right Arrow
        pyautogui.hotkey('alt', 'right')

    os_action_map = {
    "Windows": windows_action,
    "Darwin": macos_action,
    "Linux": linux_action
    }
    action = os_action_map[detect_os()]
    try:
        action()
    except:
        print("Unknown operating system. No action defined.")


def previous_track():
    def windows_action():
        # Simulate pressing the 'Previous Track' multimedia key
        pyautogui.press('prevtrack')
        pyautogui.press('prevtrack')

    def macos_action():
        # Simulate pressing Control + Command + Left Arrow
        pyautogui.hotkey('ctrl', 'command', 'left')
        pyautogui.hotkey('ctrl', 'command', 'left')

    def linux_action():
        # Simulate pressing Alt + Left Arrow
        pyautogui.hotkey('alt', 'left')  
        pyautogui.hotkey('alt', 'left')  

    os_action_map = {
    "Windows": windows_action,
    "Darwin": macos_action,
    "Linux": linux_action
    }
    action = os_action_map[detect_os()]
    try:
        action()
    except:
        print("Unknown operating system. No action defined.")


def play_pause_track():
    def windows_action():
        # Simulate pressing the 'Previous Track' multimedia key
        pyautogui.press('playpause')

    def macos_action():
        # Simulate pressing Control + Command + Left Arrow
        pyautogui.hotkey('ctrl', 'command', 'space')

    def linux_action():
        # Simulate pressing Alt + Left Arrow
        pyautogui.hotkey('alt', 'p')  

    os_action_map = {
    "Windows": windows_action,
    "Darwin": macos_action,
    "Linux": linux_action
    }
    action = os_action_map[detect_os()]
    try:
        action()
    except:
        print("Unknown operating system. No action defined.")


def volume_up():
    def windows_action():
        # Simulate pressing the 'Volume Up' multimedia key
        pyautogui.press('volumeup')

    def macos_action():
        # Simulate pressing Control + Command + Up Arrow
        pyautogui.hotkey('ctrl', 'command', 'up')

    def linux_action():
        # Simulate pressing Alt + Up Arrow 
        pyautogui.hotkey('alt', 'up')  

    os_action_map = {
        "Windows": windows_action,
        "Darwin": macos_action,
        "Linux": linux_action
    }
    action = os_action_map[detect_os()]
    try:
        action()
    except:
        print("Unknown operating system. No action defined.")


def volume_down():
    # Simulate pressing the 'Volume Down' multimedia key
    def windows_action():
        pyautogui.press('volumedown')

    # Simulate pressing Control + Command + Down Arrow
    def macos_action():
        pyautogui.hotkey('ctrl', 'command', 'down')

    # Simulate pressing Alt + Down Arrow 
    def linux_action():
        pyautogui.hotkey('alt', 'down')

    os_action_map = {
        "Windows": windows_action,
        "Darwin": macos_action,
        "Linux": linux_action
    }
    action = os_action_map[detect_os()]
    try:
        action()
    except:
        print("Unknown operating system. No action defined.")



