
import tkinter as tk

from tkinter import *
# from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import ImageTk,Image

window = tk.Tk()

label = tk.Label(
    text="Welcome to RochePath",
    foreground="white",  # Set the text color to white
    background="blue",  # Set the background color to black
    width=20,
    height=10
)

button = tk.Button(
    text="Load Image",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

# label = tk.Label(text="Hello, Tkinter", fg="white", bg="black")
label.pack()
button.pack()
window.mainloop()