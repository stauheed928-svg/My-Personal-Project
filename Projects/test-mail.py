import smtplib
from takecommand import*
import pyttsx3

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait() 

# speak ("Enter your mail")
x = input("Enter your Gmail ID\n",)
# y = takecommand()
y = speak ("What shoud i send",input("Enter your mail\n"))

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('tauheedsiddiqui396@gmail.com','pkej kndm fxye rhvq')

    # content = takecommand()
    server.sendmail('tauheedsiddiqui396@gmail.com',to,content)
    server.close()
    print("email sent")

sendEmail(x,y)

# just frinde emails : 1) muzzammilsayyed9@gmail.com
#                      2) jaikale07@gmail.com
#                       3) tauheedsiddiqui396@gmail.com
#                       4) ammarsiddiqui9960@gmail.com
#                       