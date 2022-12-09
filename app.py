from tkinter import Tk, Canvas, Button, Menu, Label, filedialog, Frame, YES, NO, BOTH
from PIL import ImageTk, Image
from PIL.ImageTk import PhotoImage
import csv

TITLE = "Roche Tissue Image"
IMAGE_PATH = "Pytorch-UNet-master/Tissue_Images"
# DEFAULT_IMAGE_PATH = "resources/roche.png"


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


def export(file_path, data, fields=None):
    with open(file_path, "w") as f:
        write = csv.writer(f)
        if fields:
            write.writerow(fields)
        write.writerows(data)


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

        self.buttons = self.create_buttons()
        self.menu = self.create_menu()
        self.root.config(menu=self.menu)

        self.coordinates = []
        self.bind_click_event()
        self.update()
        self.root.mainloop()

    def bind_click_event(self):
        def callback(event):
            coordinate = canvas_to_image_cords(self.canvas, event.x, event.y, self.image)
            print("Coordinate:", coordinate, "RGB:", self.pil_image.getpixel(coordinate))
            self.coordinates.append(coordinate)

        self.canvas.bind("<Button-1>", callback)

    def create_menu(self):
        menubar = Menu(self.root)
        file = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file)
        file.add_command(label="Open...", command=self.open_image)
        file.add_separator()
        file.add_command(label="Export coordinates to CSV...", command=self.export_coordinates_to_csv)
        return menubar

    def create_buttons(self):
        buttons = dict()
        # buttons["open"] = Button(self.root, text="Open File", command=lambda: self.open_image())
        buttons["export"] = Button(self.root, text="Export",
                                   command=lambda: self.export_coordinates_to_csv(use_filedialog=False))
        return buttons

    def open_image(self):

        self.coordinates.clear()
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

    def export_coordinates_to_csv(self, use_filedialog=True):

        file_path = "./output.csv"
        if use_filedialog:
            default_extension = [("csv file(*.csv)", "*.csv"), ('All tyes(*.*)', '*.*'), ]
            file_path = filedialog.asksaveasfilename(filetypes=default_extension, defaultextension=default_extension)

        fields = ['X', 'Y']
        export(file_path, self.coordinates, fields)
        print("Save POIs coordinates to", file_path)


if __name__ == "__main__":
    gui = MyGUI()
