import google.generativeai as genai 
import os
from dotenv import load_dotenv
load_dotenv()


def gemini_model_response(user_input):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY")) 
    model = genai.GenerativeModel("gemini-2.5-flash") 
    prompt = f"Your name is JARVIS, You act like JARVIS. Answar the provided question in short, Question: {user_input}"
    response = model.generate_content(prompt)
    result = response.text

    return result

