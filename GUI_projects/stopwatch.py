import tkinter as tk
import time

class StopwatchAPP:
    def __init__(self,root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.geometry("250x200")
        self.root.resizable(False,False)
        self.running = False
        self.elapsed_time = 0

        self.time_label = tk.Label(root,text="0:00:00",font=("heletica",48),bg="Black",fg="red")
        self.start_button = tk.Button(root,text="Start",bg="Black",fg="#fff",command=self.Start_Stop)
        self.reset_button = tk.Button(root,text="Reset",bg="Black",fg="#fff",command=self.reset)

        self.time_label.pack(pady=20)
        self.start_button.pack(pady=10)
        self.reset_button.pack(pady=3)
        self.update_time()

    def Start_Stop(self):
        self.running = not self.running
        if self.running:
            self.start_button.config(text="Stop")
            self.start_time = time.time() - self.elapsed_time
        else:
            self.start_button.config(text="Start")
            self.elapsed_time = time.time() - self.start_time

    def reset(self):
        self.running = False
        self.start_button.config(text="Start")
        self.elapsed_time = 0
        self.update_time()

    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
        minutes,second = divmod(int(self.elapsed_time),60)
        hours,minutes = divmod(minutes,60)
        self.time_label.config(text=f"{hours}:{minutes:02}:{second:02}")
        self.root.after(1000,self.update_time)

__name__ == "__main__"
root = tk.Tk()
app = StopwatchAPP(root)
root.mainloop()