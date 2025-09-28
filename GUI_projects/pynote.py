from tkinter import*
from tkinter import ttk
from tkinter import filedialog,messagebox
from tkinter.scrolledtext import ScrolledText

class python:
    def __init__(self,root):
        self.root = root

        # lablel = ttk.Label(text = "Write Your Note's" )
        # lablel.pack()

        menubar = Menu(self.root)
        filemenu = Menu(menubar,tearoff=0)  

        filemenu.add_command(label="New",command=None)
        filemenu.add_command(label= "Open",command=None)
        filemenu.add_command(label= "Save",command=None)

        filemenu.add_separator()
        filemenu.add_command(label= "Quit",command=root.destroy)

        menubar.add_cascade(label="File",command=self.root)
        self.root.config(menu=menubar)
        
        


        # output = tk.Text(root, height=17,width=50, wrap=tk.WORD)
        # output.pack()

    if __name__ == "__main__":
        root = Tk()
        root.title("GUI Notpad")
        root.geometry("500x400")
        root.mainloop()