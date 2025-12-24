from function.core import Text_to_speech
import datetime
import random

speak = Text_to_speech.speak

def greeting(user_name="sir"):
    now = datetime.datetime.now()
    hour = now.hour
    day = now.strftime("%A") 

    morning_greetings = [
        f"Good morning {user_name}! Hope you slept well.",
        f"Morning {user_name}! Ready for a productive day?",
        f"Hello {user_name}, good morning! Let's make today great."
    ]

    afternoon_greetings = [
        f"Good afternoon {user_name}! How's your day going?",
        f"Hello {user_name}, good afternoon! Hope you're doing well.",
        f"Afternoon {user_name}! Keep up the good work today."
    ]

    evening_greetings = [
        f"Good evening {user_name}! How was your day?",
        f"Hello {user_name}, good evening! Time to relax a bit.",
        f"Evening {user_name}! Hope you had a productive day."
    ]

    if 0 <= hour < 12:
        speak(random.choice(morning_greetings))
    elif 12 <= hour <= 18:
        speak(random.choice(afternoon_greetings))
    else:
        speak(random.choice(evening_greetings))

    speak(f"Today is {day}. I am Jarvis, your personal assistant. How may I help you?")



