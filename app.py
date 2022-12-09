from tkinter import Tk, Canvas, Button, Menu, filedialog, NO, BOTH

from PIL import ImageTk, Image
from PIL.ImageTk import PhotoImage

import csv

# Configurable fields
APP_TITLE = "Roche Tissue Image"
DEFAULT_FOLDER = "Pytorch-UNet-master/Tissue_Images"
DEFAULT_CSV_FILE_PATH = "./coordinates.csv"
DEFAULT_MARK_COLOR = "#43FF33"


# DEFAULT_IMAGE_PATH = "resources/roche.png"


def canvas_to_image_cords(canvas: Canvas, x: int, y: int, image: PhotoImage, tag_or_id=''):
    if not canvas or not image:
        return

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

    req_x, req_y = int(start_x + x), int(start_y + y)

    return req_x, req_y


def export(file_path, data, fields=None):
    with open(file_path, "w") as f:
        write = csv.writer(f)
        if fields:
            write.writerow(fields)
        write.writerows(data)


def canvas_draw_mark(canvas: Canvas, x: int, y: int, r: int = 5, mark_line_width=5, color=DEFAULT_MARK_COLOR):
    width = canvas.winfo_width()
    height = canvas.winfo_height()

    x_from = x - r if x >= r else 0
    y_from = y - r if y >= r else 0
    x_to = x + r if x + r < width else width
    y_to = y + r if y + r < height else height

    line1 = canvas.create_line(x_from, y_from, x_to, y_to, width=mark_line_width, fill=color)
    line2 = canvas.create_line(x_to, y_from, x_from, y_to, width=mark_line_width, fill=color)
    return [line1, line2]


class MyGUI(object):

    def __init__(self):
        self.root = Tk()
        self.root.title(APP_TITLE)
        self.root.geometry("1000x1100")
        self.root.resizable(width=True, height=True)

        self.canvas = Canvas(width=1000, height=1000, bg="black", bd=0)
        self.canvas.pack(expand=NO, fill=BOTH)
        self.drawings = []

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
            if not self.image:
                return

            coordinate = canvas_to_image_cords(self.canvas, event.x, event.y, self.image)
            print("Coordinate:", coordinate, "RGB:", self.pil_image.getpixel(coordinate))
            self.coordinates.append(coordinate)

            self.drawings.extend(canvas_draw_mark(self.canvas, event.x, event.y, 5))

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
        self.image_path = filedialog.askopenfilename(initialdir=DEFAULT_FOLDER, title="Tissue Images",
                                                     filetypes=(("All files", "*.*"), ("tiff", "*.tiff")))
        print("Open image file:", self.image_path)
        self.open_image_path(self.image_path)

        self.coordinates.clear()
        self.clear_canvas_drawings()
        self.update()

    def open_image_path(self, file_path):
        self.pil_image = Image.open(file_path)
        self.image = ImageTk.PhotoImage(self.pil_image)
        if self.image_canvas_object:
            self.canvas.itemconfig(self.image_canvas_object, image=self.image)
        else:
            self.image_canvas_object = self.canvas.create_image(0, 0, image=self.image, anchor="nw")

    def clear_canvas_drawings(self):
        for x in self.drawings:
            self.canvas.delete(x)

    def update(self):
        for btn in self.buttons.values():
            btn.pack()

    def export_coordinates_to_csv(self, use_filedialog=True):

        file_path = DEFAULT_CSV_FILE_PATH
        if use_filedialog:
            default_extension = [("csv file(*.csv)", "*.csv"), ('All tyes(*.*)', '*.*'), ]
            file_path = filedialog.asksaveasfilename(filetypes=default_extension, defaultextension=default_extension)

        fields = ['X', 'Y']
        export(file_path, self.coordinates, fields)
        print("Save PoI coordinates to file:", file_path)


if __name__ == "__main__":
    gui = MyGUI()
