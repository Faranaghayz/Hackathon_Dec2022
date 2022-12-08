# Import Module
from tkinter import Tk, Canvas, Button, Label, filedialog, Frame
from PIL import ImageTk, Image
from PIL.ImageTk import PhotoImage

TITLE = "Welcome to GeekForGeeks"
IMAGE_PATH = "Pytorch-UNet-master/Tissue_Images"


class MyGUI(object):

    def __init__(self):
        self.root = Tk()
        self.root.title(TITLE)
        self.root.geometry('1000x1200')
        self.canvas = Canvas(width=1000, height=1000, bg="black", bd=0)
        self.canvas.pack()

        self.image = None
        self.image_path = ""
        self.image_canvas_object = None

        self.buttons = self.create_buttons()
        self.labels = self.create_labels()

        self.update()
        self.root.mainloop()

    def create_buttons(self):
        buttons = dict()
        buttons["open"] = Button(self.root, text="Open File", command=lambda: self.open_image())
        return buttons

    def create_labels(self):
        labels = dict()
        # labels["image"] = Label(self.root, self.image)
        return labels

    def open_image(self):
        self.image_path = filedialog.askopenfilename(initialdir=IMAGE_PATH, title="Tissue Images",
                                                     filetypes=(("All files", "*.*"), ("tiff", "*.tiff")))
        self.image = ImageTk.PhotoImage(Image.open(self.image_path))

        if self.image_canvas_object:
            self.canvas.itemconfig(self.image_canvas_object, image=self.image)
        else:
            self.image_canvas_object = self.canvas.create_image(1000, 1000, image=self.image)

        self.update()

    def update(self):
        for btn in self.buttons.values():
            btn.pack()

        for label in self.labels.values():
            label.pack()


if __name__ == "__main__":
    gui = MyGUI()

#
# def open_image():
#     global root, image, label_image, label_image_file
#     root.filename = filedialog.askopenfilename(initialdir=IMAGE_PATH, title="Tissue Images",
#                                                filetypes=(("All files", "*.*"), ("tiff", "*.tiff")))
#
#     image = ImageTk.PhotoImage(Image.open(root.filename))
#     label_image = Label(root, image=image)
#     label_image_file.text = root.filename
#
#     label_image.pack()
#     # label_image_file.pack()
#
#
# root = Tk()
# root.title(TITLE)
# root.geometry('1000x1200')
#
#
# image = ImageTk.PhotoImage(file="Pytorch-UNet-master/Tissue_Images/TCGA-18-5592-01Z-00-DX1.tif")
# label_image = Label(root, image=image)
# label_image_file = Label(root)
# btn_open = Button(root, text="Open File", command=lambda: open_image())
#
# label_image_file.pack()
# label_image.pack()
# btn_open.pack()
#
# # all widgets will be here
# # Execute Tkinter
# root.mainloop()
