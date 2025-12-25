import pyautogui
import time 
import webbrowser
import keyboard
import pyperclip

time.sleep(3)
search_query = "python datatypes"

webbrowser.open("https://www.youtube.com")
time.sleep(4) 

pyautogui.click(x=866, y=112)
keyboard.write(search_query)
keyboard.press_and_release('enter')

# Alternative: Search icon-e click kora
# time.sleep(2)
# pyautogui.click(x=1161, y=110)
# print(pyautogui.position())


pyautogui.click(x=667, y=158) 
time.sleep(3)
pyautogui.click(x=792 , y=527)


# 4. Wait for video to open and copy URL
time.sleep(3)
pyautogui.hotkey('ctrl', 'l') # Highlight address bar
pyautogui.hotkey('ctrl', 'c') # Copy

video_url = pyperclip.paste()
print(f"The link is: {video_url}")

print(pyautogui.position())


