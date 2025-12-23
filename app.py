import google.generativeai as genai
import pyttsx3
import logging 
import os 
import datetime 
import wikipedia 
import webbrowser
import random
import subprocess
import speech_recognition as sr

# logging configuration 
LOG_DIR = 'logs'
LOG_FILE_NAME = "application.log"

os.makedirs(LOG_DIR , exist_ok=True)

log_path = os.path.join(LOG_DIR , LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)


# Activating voice from our system 
engine = pyttsx3.init("sapi5") 
engine.setProperty('rate', 170)
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[0].id)


# This is speak function
def speak(text):
    """This function converts text to voice

    Args:
        text
    returns:
        voice
    """
    engine.say(text)
    engine.runAndWait()

# This function recognize the speech and convert it to text 

def takeCommand():
    """This function takes command & recognize

    Returns:
        text as query
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...") 
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        logging.info(e)
        print("Say that again please")
        return "None"
    
    return query


def greeting():
    hour = (datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir! How are you doing?")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon sir! How are you doing?")
    else:
        speak("Good Evening sir! How are you doing?")
    

    speak("I am Jarvis. Please tell me how may I help you today?")


# def play_music():
#     music_dir = ""   # <-- change this to your music folder
#     try:
#         songs = os.listdir(music_dir)
#         if songs:
#             random_song = random.choice(songs)
#             speak(f"Playing a random song sir: {random_song}")
#             os.startfile(os.path.join(music_dir, random_song))
#             logging.info(f"Playing music: {random_song}")
#         else:
#             speak("No music files found in your music directory.")
#     except Exception:
#         speak("Sorry sir, I could not find your music folder.")


def gemini_model_response(user_input):
    GEMINI_API_KEY = "your api key here"
    genai.configure(api_key=GEMINI_API_KEY) 
    model = genai.GenerativeModel("gemini-2.5-flash") 
    prompt = f"Your name is JARVIS, You act like JARVIS. Answar the provided question in short, Question: {user_input}"
    response = model.generate_content(prompt)
    result = response.text

    return result


greeting()


