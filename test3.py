
from tkinter import *
# from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import ImageTk,Image

root=Tk()
root.title('RochePath')

my_img=ImageTk.PhotoImage(Image.open("Pytorch-UNet-master/Tissue_Images/TCGA-18-5592-01Z-00-DX1.tif"))
my_label=Label(image=my_img)
my_label.pack()
root.mainloop()


## another
app = Tk()
app.geometry("400x400")

canvas = Canvas(app, bg='black')
canvas.pack(anchor='nw', fill='both', expand=1)
image = Image.open("img.tif")
image = image.resize((400,400), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)
canvas.create_image(0,0, image=image, anchor='nw')
label = Label(
    text="Welcome to RochePath",
    foreground="white",  # Set the text color to white
    background="blue",  # Set the background color to black
    width=20,
    height=10
)

button = Button(
    text="Load Image",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)


app.mainloop()


def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y

def draw_smth(event):
    global lasx, lasy
    canvas.create_line((lasx, lasy, event.x, event.y),
                      fill='red',
                      width=2)
    lasx, lasy = event.x, event.y

canvas.bind("<Button-1>", get_x_and_y)
canvas.bind("<B1-Motion>", draw_smth)

app.mainloop()
