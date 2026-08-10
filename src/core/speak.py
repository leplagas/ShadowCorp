import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    print(f"Speaking: {text}")
    engine.say(text)
    engine.runAndWait()