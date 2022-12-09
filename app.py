# Import Module
from tkinter import Tk, Canvas, Button, Label, filedialog, Frame, YES, NO, BOTH
from PIL import ImageTk, Image
from PIL.ImageTk import PhotoImage

TITLE = "Welcome to GeekForGeeks"
IMAGE_PATH = "Pytorch-UNet-master/Tissue_Images"
DEFAULT_IMAGE_PATH = "resources/roche.png"


def canvas_to_image_cords(canvas: Canvas, x: int, y: int, image: PhotoImage, tag_or_id=''):
    anchor = 'center'
    if tag_or_id:
        anchor = canvas.itemcget(tag_or_id, 'anchor')

    w, h = canvas.winfo_reqwidth(), canvas.winfo_reqheight()

    if anchor == 'center':
        img_xpos, img_ypos = image.width() / 2, image.height() / 2
        start_x, start_y = img_xpos - w / 2, img_ypos - h / 2
    elif anchor == 'nw':
        start_x, start_y = 0, 0
    # And so on for different anchor positions if you want to make this more modular

    req_x, req_y = start_x + x, start_y + y

    return req_x, req_y


class MyGUI(object):

    def __init__(self):
        self.root = Tk()
        self.root.title(TITLE)
        self.root.geometry("1000x1100")
        self.root.resizable(width=True, height=True)

        self.canvas = Canvas(width=1000, height=1000, bg="black", bd=0)
        self.canvas.pack(expand=NO, fill=BOTH)

        self.pil_image = None
        self.image = None
        self.image_path = None
        self.image_canvas_object = None
        # self.open_image_path(DEFAULT_IMAGE_PATH)

        self.buttons = self.create_buttons()
        # self.labels = self.create_labels()

        self.bind_click_event()
        self.update()
        self.root.mainloop()

    def bind_click_event(self):
        def callback(event):
            # print("[Canvas] clicked at", event.x, event.y)
            coordinate = canvas_to_image_cords(self.canvas, event.x, event.y, self.image)
            print("Coordinate:", coordinate, "RGB:", self.pil_image.getpixel(coordinate))

        self.canvas.bind("<Button-1>", callback)

    def create_buttons(self):
        buttons = dict()
        buttons["open"] = Button(self.root, text="Open File", command=lambda: self.open_image())
        return buttons

    # def create_labels(self):
    #     labels = dict()
    #     return labels

    def open_image(self):

        self.image_path = filedialog.askopenfilename(initialdir=IMAGE_PATH, title="Tissue Images",
                                                     filetypes=(("All files", "*.*"), ("tiff", "*.tiff")))
        self.open_image_path(self.image_path)
        self.update()

    def open_image_path(self, file_path):
        self.pil_image = Image.open(file_path)
        self.image = ImageTk.PhotoImage(self.pil_image)
        if self.image_canvas_object:
            self.canvas.itemconfig(self.image_canvas_object, image=self.image)
        else:
            self.image_canvas_object = self.canvas.create_image(0, 0, image=self.image, anchor="nw")

    def update(self):
        for btn in self.buttons.values():
            btn.pack()

        # for label in self.labels.values():
        #     label.pack()


if __name__ == "__main__":
    gui = MyGUI()
