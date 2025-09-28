from tkinter import*
from tkinter import ttk
import tkinter as tk
import cv2
from PIL import Image,ImageTk
import os
import smtplib
import pyttsx3
import time
import datetime 
from datetime import date                 
import wikipedia
import webbrowser
import random
import string
import pyjokes
import pyttsx3
import speech_recognition as sr 

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
    print("The curren Time is"+time)
    speak("The curren Time is"+time)
def date():
    Date = str(datetime.date.today())
    print("Today's Date is"+Date)
    speak("Today's Date is"+Date)
def dice():
    def change_text():
        random_num = random.randint(1,6)
        img_dice = f"{random_num}.png"
        img = Image.open(img_dice)
        img = ImageTk.PhotoImage(img)
        label.config(image=img)
        label.image = img
    root = Tk()
    root.geometry("500x500")
    root.title("Dice APP")
    label = ttk.Label(text = "Roll a Dice")
    label.pack()
    button1 = ttk.Button(text = "Roll",command=change_text)
    button1.pack()
    button = ttk.Button(text = "Quit",command=root.destroy)
    button.pack()
    root.mainloop()
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
    # print("Entwr Number 1:")
    # speak("Entwr Number 1:")
    # x = takecommand()
    # print("Entwr Number 2:")
    # speak("Entwr Number 2:")
    # y = takecommand()
    # print("The Optration:")
    # speak("The Optration:")
    # z = takecommand()
    speak("Entwr Number 1:")
    x = int(input ("Entwr Number 1:\n"))
    speak("Entwr Number 2:")
    y = int(input ("Entwr Number 2:\n"))
    speak("The Optration:")
    z = (input ("The Optration:\n"))
    if ("1") in z or "add" in z or "+" in z:
        sum = x + y
        speak (f"The sum the numbers is:\n {sum}")
        print(f"The sum the numbers is:\n {sum}")
    elif ("2") in z or "sub" in z or "-" in z:
        sum = x - y
        speak(f"The sum the numbers is:\n{sum}")
        print(f"The sum the numbers is:\n{sum}")
    elif ("3") in z or "mult" in z or "*" in z:
        sum = x * y
        speak(f"The sum the numbers is:\n{sum}")
        print(f"The sum the numbers is:\n{sum}")
    elif ("4") in z or "divid" in z or "/" in z:
        sum = x / y
        speak(f"The sum the numbers is:\n{sum}")
        print(f"The sum the numbers is:\n{sum}")
    elif ("5") in z or "mod" in z or "%" in z:
        sum = x % y
        speak(f"The sum the numbers is:\n{sum}")
        print(f"The sum the numbers is:\n{sum}")
    else:
        speak("Plz Enter valid number betweeen 1 to 5")
        print("Plz Enter valid number betweeen 1 to 5")
def jokes():
    speak(pyjokes.get_joke())
def camera():

    class webcamAPP:
        def __init__(self,window):
            self.window = window
            self.window.title("Webcam App")
            
            self.video_capture = cv2.VideoCapture(0)
            self.current_image = None
            self.canvas = tk.Canvas(window, width=600,height=450)
            self.canvas.pack()

            def caputure(self,window):
                while True:
                    speak("Ask Question\n")
                    x = takecommand()
                    self.download_button = tk.Button(window,text="Capture",command=self.download_image )
                    self.download_button.pack()

            self.exit_button = tk.Button(window,text="Exit",command=root.destroy)
            self.exit_button.pack()

            self.update_Webcam()
            

        def update_Webcam(self):
            ret,frame = self.video_capture.read()

            if ret:
                self.current_image = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))

                self.photo = ImageTk.PhotoImage(image=self.current_image)

                self.canvas.create_image(0,0,image=self.photo,anchor=tk.NW)

                self.window.after(15,self.update_Webcam)
    
        def download_image(self):
            if self.current_image is not None:
                file_path = os.path.expanduser("~/Downloads/capture_image.jpg")
                self.current_image.save(file_path)
                os.startfile(file_path)

    root = tk.Tk()
    app = webcamAPP(root)
    root.mainloop()
def email():

    engine = pyttsx3.init()

    def speak(text):
        engine.say(text)
        engine.runAndWait() 
    speak ("Enter your Gmail ID")
    x = input("Enter your Gmail ID\n")
    speak ("Enter your mail")
    y = takecommand()
    # y = ("Enter your mail\n")
    def sendEmail(to,content):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('tauheedsiddiqui396@gmail.com','pkej kndm fxye rhvq')
        # content = takecommand()
        server.sendmail('tauheedsiddiqui396@gmail.com',to,content)
        server.close()
        print("email sent")
    sendEmail(x,y) 
while (True):
    speak("Ask Question\n")
    x = takecommand()
    x = x.lower()
    if "hi" in x:
        speak("Hello, I'm your 'AI BOT',How may i help you")
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
    elif "camera" in x:
       camera()
    elif "mail" in x:
       email()           
    elif "exit" in x:
        break
    else: 
        speak("Plz give valid info")

