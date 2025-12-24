from function.core import Text_to_speech
import json
speak = Text_to_speech.speak

# Load jokes from a JSON file
with open("python_jokes.json") as f:
    jokes = json.load(f)

# Example: speak a random joke
import random
speak(random.choice(jokes)["joke"])
