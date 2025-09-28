from tkinter import*
from tkinter import filedialog

root = Tk()
root.title("Notpad")
root.geometry("600x500")
root.resizable(False,False)
root.config(bg="Light Blue")

def save_file():
    open_file=filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if open_file is None:
        return
    text=str(entery.get(1.0,END))
    open_file.write(text)
    open_file.close()

def open_file():
    file=filedialog.askopenfile(mode="r",filetypes=[("text file","*.txt")]) 
    if file is not None:
        content=file.read()
    entery.insert(INSERT,content)


b1 = Button(root,width=20,height=2,text="Save",bg="#fff",command=save_file).place(x=100,y=10 )
b2= Button(root,width=20,height=2,text="Open",bg="#fff",command=open_file ).place(x=350,y=10)

entery = Text(root,height=25,width=72,wrap=WORD)
entery.place(x=10,y=70)

root.mainloop()