from function.core import  Text_to_speech
import wikipedia
from function import gemini_model
import logging

gemini_model_response = gemini_model.gemini_model_response
speak = Text_to_speech.speak


def wikipedia_summarizer(query):
    speak("Summarizing from wikipedia ")
    query = query.replace("wikipedia" , "")
    results = wikipedia.summary(query , sentence=10)
    user_input = f"Create a 2 line summary using these sentences {results}"
    gemini_model_response(user_input)
    speak(gemini_model_response)

def wikipedia_ans(query):
    speak("Searching wikipedia")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    speak(results)
    logging.info("User requested information from Wikipedia.") 

