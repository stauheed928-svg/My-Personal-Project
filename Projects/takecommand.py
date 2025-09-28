import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait() 

def takecommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...!")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Recognizing...!")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}")
    except Exception as e:
        print(e)
        speak("Please try again")
        return "None"
    return 

