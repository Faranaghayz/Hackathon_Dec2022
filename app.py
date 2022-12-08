# Import Module
from tkinter import Tk, Canvas, Button, Label, filedialog
from PIL import ImageTk, Image

PATH = "C:\\Users\\aghaeif\\Documents\\Hackathon_Dec2022\\Pytorch-UNet-master\\Tissue_Images\\"


def init_main_window():
    # create root window
    root = Tk()

    # root window title and dimension
    root.title("Welcome to GeekForGeeks")

    # Set geometry (widthxheight)
    root.geometry('800x600')
    return root


# def load_image(root, file_path):
#     canvas = Canvas(root, width=300, height=300)
#     canvas.pack()
#     img = PhotoImage(file=file_path)
#     canvas.create_image(20, 20, anchor=NW, image=img)
#     return root


def open(root):
    global my_image

    root.filename = filedialog.askaskopenfilename(initialdir="Pytorch-UNet-master/Tissue_Images", title="Tissue Images",
                                                  filetypes=(("All files", "*.*"), ("tiff", "*.tiff")))
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


app = init_main_window()

my_btn = Button(app, text="Open File", command=open).pack()

# load_image(app, PATH + "TCGA-18-5592-01Z-00-DX1.tif")

# all widgets will be here
# Execute Tkinter
app.mainloop()
