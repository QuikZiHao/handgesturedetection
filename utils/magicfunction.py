import pyautogui
import time
from checkOS import detect_os

def do_copy():
    time.sleep(1)
    pyautogui.hotkey('ctrl','c')


def do_paste():
    time.sleep(1)
    pyautogui.hotkey('ctrl','v')


def do_screenshot():
    screenshot = pyautogui.screenshot()
    


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

    def macos_action():
        # Simulate pressing Control + Command + Left Arrow
        pyautogui.hotkey('ctrl', 'command', 'left')

    def linux_action():
        # Simulate pressing Alt + Left Arrow
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

previous_track()