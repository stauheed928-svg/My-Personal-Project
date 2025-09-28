from tkinter import Label,Tk
import time


root = Tk()
root.title("Digital Clock")
root.geometry("420x150")
root.resizable(1,1)
text_font=("Boulder",68,"bold")
background='Black'
foreground='Red'##d46329
border_width = 25
label = Label(root,font=text_font,bg=background,fg=foreground,bd=border_width)
label.grid(row=0,column=1)

def clock():
    Time = time.strftime("%H:%M:%S")
    label.config(text=Time)
    label.after(200,clock)
clock()

root.mainloop()