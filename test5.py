def open_file():
    """Open an image for nuclei segmenting."""
    # image = Image.open("img.tif")

    filepath = askopenfilename(
        filetypes=[("tif Files", "*.tif"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        my_img = Image.open(input_file)
    window.title(f"Simple Text Editor - {filepath}")

def get_x_and_y(event):
    global lasx, lasy
    lasx, lasy = event.x, event.y