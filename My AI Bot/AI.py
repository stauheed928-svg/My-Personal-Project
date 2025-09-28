#  Total Function 
#  " Time & Date " , "Dice" , "PASSWORD" 
#  "WEB BROWSER" , " WIKIPEDIA BROWSER"
#  " CALCULATOR "
import datetime 
from datetime import date                 
import wikipedia
import webbrowser
import random
import string
import pyjokes
import pyttsx3
import speech_recognition as sr # pip install SpeechRecognition
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
    return query
def time():
    time = datetime.datetime.now().strftime("%Hhour%Mminute%Sseconds")
    speak("The curren Time is"+time)
    # print(time)
def date():
    Date = str(datetime.date.today())
    # print(Date)
    speak("Today's Date is"+Date)
def dice():
    speak(random.randint(1,6))
def password():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    s5 = s1+s2+s3+s4
    s =[]
    s.extend(s5)
    generated_password = random.shuffle(s)
    print("".join(s[0:8]))
def web():
    speak("Enter the website name:\n")
    url = takecommand()
    # url = input(speak("Enter the website name:\n"))
    webbrowser.open("https://www.google.com/search?q="+url)
def wiki():
    speak("What should I search on wikipedia\n")
    wiki = takecommand()
    # wiki = input(speak("What should I search on wikipedia\n"))
    speak(wikipedia.summary(wiki))
def cal():
    x = int(input(speak("Entwr Number 1:\n")))
    y = int(input(speak("Entwr Number 2:\n")))
    z = (input(speak("The Optration:\n")))
    if ("1") in z or "add" in z or "+" in z:
        sum = x + y
        speak(f"The sum the numbers is:\n {sum}")
    elif ("2") in z or "sub" in z or "-" in z:
        sum = x - y
        speak(f"The sum the numbers is:\n{sum}")
    elif ("3") in z or "mult" in z or "*" in z:
        sum = x * y
        speak(f"The sum the numbers is:\n{sum}")
    elif ("4") in z or "divid" in z or "/" in z:
        sum = x / y
        speak(f"The sum the numbers is:\n{sum}")
    elif ("5") in z or "mod" in z or "%" in z:
        sum = x % y
        speak(f"The sum the numbers is:\n{sum}")
    else:
        speak("Plz Enter valid number betweeen 1 to 5")
def jokes():
    speak(pyjokes.get_joke())
while True:
    speak("Ask Question\n")
    x = takecommand().lower()
    # x = input(speak("Ask Question\n"))
    if "hi" in x:
        speak("Hello, I'm your vitu,How may i help you")
    elif "time" in x:
        time()
    elif "date" in x:
        date()   
    elif "dice" in x:
        dice()
    elif "password" in x:
        password()
    elif "web" in x :
        web()
    elif "wiki" in x:
        wiki()
    elif "cal" in x:    
        cal()
    elif "jokes" in x:
       jokes()
    elif "offline" in x:
        exit()
    # elif "stop" or "exit" in x:
    #     break 
    else: 
        speak("Plz give valid info")
