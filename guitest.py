

import tkinter as tk
from tkinter.filedialog import askopenfilename

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

# ...

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

button.bind("<Button-1>", open_file)
label.pack()
window.mainloop()

# label = tk.Label(text="Hello, Tkinter", fg="white", bg="black")
label.pack()
window.mainloop()



entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()
name = entry.get()
entry.delete(0, tk.END)

# Getting Multiline User Input With Text Widgets
# Text widgets
# >>> window = tk.Tk()
# >>> text_box = tk.Text()
# >>> text_box.pack()



import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100, height=100, bg="red")
frame1.pack()

frame2 = tk.Frame(master=window, width=50, height=50, bg="yellow")
frame2.pack()

frame3 = tk.Frame(master=window, width=25, height=25, bg="blue")
frame3.pack()

window.mainloop()


def handle_click(event):
    print("The button was clicked!")

button = tk.Button(text="Click me!")

button.bind("<Button-1>", handle_click)


import tkinter as tk

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"


window = tk.Tk()
btn_decrease = tk.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()


window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="-")
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+")
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()