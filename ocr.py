import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import pytesseract

root = Tk() # define Window 
root.state('zoomed')   # window will be fullsize(maximized)
root_header = tk.Label(root, text="OCR System using Tkinter",font="Bold")  
root_header.pack(pady=10)
file_name = Text(height=1, width=120, bg="white")
file_name.place(x=30, y=round(root.winfo_screenheight()*70/100)+70)
canvas = Canvas(root, width=round(root.winfo_screenwidth()*70/100), height=round(root.winfo_screenheight()*70/100), bd=2, highlightbackground="black", bg="white", highlightthickness=1)
canvas.place(x=30,y=50)
root_text = Text(height=33, width=40)
root_text.place(x=round(root.winfo_screenwidth()/1.5)+100,y=50)
def showimg(filename):
    global img1  # Keep a reference to the img object
    img=Image.open(filename)
    resize_img=img.resize((round(img.width*70/100),round(img.height*70/100)))
    print(resize_img.height)
    img1 = ImageTk.PhotoImage(resize_img)
    canvas.config(height=resize_img.height,width=resize_img.width)
    canvas.create_image(0, 0, anchor=NW, image=img1)
    file_name.insert("end", filename)  # Use "end" instead of "10.0"
def ocr():
    image = Image.open(filename)
    text = pytesseract.image_to_string(image,lang="eng+hin+mar")
    root_text.insert("end", text)  # Use "end" instead of "10.0"
def browse():
    global filename #keep stored filename globally
    filename = filedialog.askopenfilename(initialdir='/')
    showimg(filename)    

browse_button = tk.Button(text="Browse Image", command=browse)
ocr_button=tk.Button(text="Get Text",command=ocr)
browse_button.place(x=round(root.winfo_screenwidth()/4),y=round(root.winfo_screenheight()/1.2))
ocr_button.place(x=round(root.winfo_screenwidth()/3),y=round(root.winfo_screenheight()/1.2))

root.mainloop()
