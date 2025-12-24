
import pyttsx3
# This is speak function
def speak(text):
    """This function converts text to voice

    Args:
        text
    returns:
        voice
    """ 
    # Activating voice from our system 
    engine = pyttsx3.init("sapi5") 
    engine.setProperty('rate', 170)
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()