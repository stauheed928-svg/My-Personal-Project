#  Total Function 
#  " Time & Date " , "Dice" , "PASSWORD" 
#  "WEB BROWSER" , " WIKIPEDIA BROWSER"
#  " CALCULATOR "
import datetime 
import tkinter as tk
from PIL import Image,ImageTk
import os
from datetime import date                 
import wikipedia
import webbrowser
import random
import cv2
import time
import string
import pyjokes
import smtplib
import pyttsx3

# Initialize pyttsx3 engine once
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', int(rate * 0.85))  # Adjust for slower speech
engine.setProperty('volume', 1.5)  # Max volume
import speech_recognition as sr # pip install SpeechRecognition

def speak(text):
    import time
    time.sleep(0.1)  # Short pause before speaking
    engine.say(' ')  # Dummy phrase to flush engine
    engine.runAndWait()
    engine.say(text)
    engine.runAndWait()
def get_current_time():
    current_time = datetime.datetime.now().strftime("%Hhour%Mminute%Sseconds")
    print("The current Time is "+current_time)
    speak("The current Time is "+current_time)
def date():
    Date = str(datetime.date.today())
    print("Today's Date is "+Date)
    speak("Today's Date is "+Date)
def dice():
    result = random.randint(1,6)
    print("Dice rolled: "+str(result))
    speak("Dice rolled: "+str(result))
def password():
    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation
    s5 = s1+s2+s3+s4
    s =[]
    s.extend(s5)
    generated_password = random.shuffle(s)
    print(speak("the password is "), "".join(s[0:8]))
def web():
    speak("Enter the website name")
    # url = takecommand()
    url = input(speak("Enter the website name:\n"))
    webbrowser.open("https://www.google.com/search?q="+url)
def wiki():
    # speak("What should I search on wikipedia\n")
    # wiki = takecommand()
    wiki = input(speak("What should I search on wikipedia\n"))
    summary = wikipedia.summary(wiki)
    print(summary)
    speak("Reading Wikipedia summary. Say 'stop' to interrupt.")
    for sentence in summary.split('. '):
        speak(sentence)
        user_input = input("Type 'stop' to interrupt or press Enter to continue:\n").lower()
        if user_input == "stop":
            speak("Stopped reading Wikipedia summary.")
            break
def email():
    engine = pyttsx3.init()
    def speak(text):
        engine.say(text)
        engine.runAndWait()
    speak("Enter your Gmail ID")
    x = input("Enter your Gmail ID\n")
    speak ("Enter your mail")
    # y = takecommand()
    speak ("Enter What you want to send")
    y = input("Enter your mail\n")
    def sendEmail(to,content):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('tauheedsiddiqui396@gmail.com','pkej kndm fxye rhvq')
        server.sendmail('tauheedsiddiqui396@gmail.com',to,content)
        server.close()
        speak("email sent")
        print("email sent")
    sendEmail(x,y) 
def cam():
    cam = cv2.VideoCapture(0)
    while True:
        ret, frame = cam.read()
        cv2.imshow("webcam", frame)
        key = cv2.waitKey(1)
        if key == ord('c'):
            newtime = str(time.time())
            cv2.imwrite(f"{newtime}.png", frame)
        elif key == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
def cal():
    speak(f"Enter Number 1:\n")
    x = int(input("Enter Number 1:\n"))
    speak(f"Enter Number 2:\n")
    y = int(input("Enter Number 2:\n"))
    speak(f"Enter the operation:\n")
    print("""1 or Add or + for Addition \n2 or Sub or - Subtraction \n3 or Mult or * for Multipication \n4 or Divid or / for Division \n5 or Mod or % for Modulas """)
    z = (input("The Operation:\n"))
    if ("1") in z or "add" in z or "+" in z:
        sum = x + y
        print(f"The sum the numbers is:\n {sum}")
        speak(f"The sum the numbers is:\n {sum}")
    elif ("2") in z or "sub" in z or "-" in z:
        sum = x - y
        print(f"The sum the numbers is:\n{sum}")
        speak(f"The sum the numbers is:\n{sum}")
    elif ("3") in z or "mult" in z or "*" in z:
        sum = x * y
        print(f"The sum the numbers is:\n{sum}")
        speak(f"The sum the numbers is:\n{sum}")
    elif ("4") in z or "divid" in z or "/" in z:
        sum = x / y
        print(f"The sum the numbers is:\n{sum}")
        speak(f"The sum the numbers is:\n{sum}")
    elif ("5") in z or "mod" in z or "%" in z:
        sum = x % y
        print(f"The sum the numbers is:\n{sum}")
        speak(f"The sum the numbers is:\n{sum}")
    else:
        speak("Plz Enter valid number betweeen 1 to 5")
def jokes():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)
while True:
    speak("Hello I'm your virtual assistan nova. How may i help you?")
    x = input("Enter your command:\n").lower()
    # x = takecommand().lower() 
    if "hi" in x:
        speak("Hello I'm your virtual assistant. How may I help you?")
    elif "time" in x:
        get_current_time()
    elif "date" in x:
        date()   
    elif "dice" in x:
        dice()
    elif "password" in x or "pass" in x:
        password()
    elif "web" in x :
        web()
    elif "wiki" in x:
        wiki()
    elif "cal" in x:    
        cal()
    elif "jokes" in x:
       jokes()
    elif "cam" in x:
         cam()
    elif "mail" in x:
         email()
    elif "stop" in x or "exit" in x:
       break 
    else: 
        speak("Plz give valid info")
