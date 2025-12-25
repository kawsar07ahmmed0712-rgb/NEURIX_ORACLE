# from function.core import speech_recognization

# takeCommand = speech_recognization.takeCommand

# takeCommand() ✅ take_command is doing well



# from function.core import Text_to_speech

# speak = Text_to_speech.speak

# speak("I am good") ✅ It is also doing well



# from function import gemini_model
# from function.core import Text_to_speech

# speak = Text_to_speech.speak

# gemini_model_response = gemini_model.gemini_model_response

# speak(gemini_model_response("How to play football?"))  ✅ This is also doing well

# from function.core import play_video_audio

# play_video = play_video_audio.play_video

# play_video()



# import pyautogui
# import time

# time.sleep(3)

# import webbrowser
# import time
# import pyperclip
# import keyboard

# # # 1. Open YouTube
# search_query = "python datatypes"
# webbrowser.open("https://www.youtube.com")
# pyautogui.click(x=866 , y=112)
# keyboard.is_pressed("python database")
# time.sleep(2)
# pyautogui.click(x=1161 , y=110)

# # webbrowser.open(f"https://www.youtube.com/results?search_query={search_query}")

# # pyautogui.click(x=667, y=158) 
# # time.sleep(3)
# # pyautogui.click(x=792 , y=527)


# # # 4. Wait for video to open and copy URL
# # time.sleep(3)
# # pyautogui.hotkey('ctrl', 'l') # Highlight address bar
# # pyautogui.hotkey('ctrl', 'c') # Copy

# # video_url = pyperclip.paste()
# # print(f"The link is: {video_url}")

# # print(pyautogui.position())








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
