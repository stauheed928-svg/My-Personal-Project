import tkinter as tk
import cv2
from PIL import Image,ImageTk
import os

class webcamAPP:
    def __init__(self,window):
        self.window = window
        self.window.title("Webcam App")
        
        self.video_capture = cv2.VideoCapture(0)
        self.current_image = None
        self.canvas = tk.Canvas(window, width=600,height=450)
        self.canvas.pack()

        self.download_button = tk.Button(window,text="Capture",command=self.download_image)
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
root.geometry("450x500")
root.mainloop()