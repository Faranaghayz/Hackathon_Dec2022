
import tkinter as tk
from tkinter import Tk, Canvas, Button, Label, filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename

def open_file():
    """Open a file for editing."""

    filepath = askopenfilename(
        filetypes=[("TIF Files", "*.tif"), ("All Files", "*.*")]
    )
    my_img = ImageTk.PhotoImage(Image.open(filepath))

    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")

def annotate_file(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def mask_file():
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

def boundary_file():
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

window = tk.Tk()
window.title("RochePath")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
# window.geometry("750x270")

# txt_edit = tk.Image(window)
#Create a canvas
canvas= tk.Canvas(window, width= 600, height= 400)
canvas.pack()
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Load Image", command=open_file)
btn_annotate = tk.Button(frm_buttons, text="Start Annotation", command=annotate_file)
btn_done = tk.Button(frm_buttons, text="Generate Mask", command=mask_file)
btn_boundary = tk.Button(frm_buttons, text="Generate Boundary", command=boundary_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_annotate.grid(row=1, column=0, sticky="ew", padx=5)
btn_done.grid(row=2, column=0, sticky="ew", padx=5)
btn_boundary.grid(row=3, column=0, sticky="ew", padx=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
# txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()