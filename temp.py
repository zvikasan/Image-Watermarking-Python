# Using what you have learnt about Tkinter, you will create a desktop application with a Graphical User Interface(GUI) where you can upload an image and use Python to add a watermark logo/text.

# You might need:

# https: // pypi.org/project/Pillow/

# https: // docs.python.org/3/library/tkinter.html

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont


DARKGRAY = "#A9A9A9"
DIMGRAY = "#696969"
MIDNIGHTBLUE = "#191970"

#------------------ REMOVE LATER ------------------------
LIGHT_GREY = "#D3D3D3"
GRAY = "#BEBEBE"
VIOLET = "#EE82EE"
SKYBLUE = "#87CEEB"
SALMON = "#FA8072"
ROSYBROWN = "#BC8F81"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
#------------------------------------------

FONT_NAME = "Courier"


def openfilename():
    filename = filedialog.askopenfilename(title='Select Image')
    return filename


def open_img():
    global img
    global loaded_image
    selected_img = filedialog.askopenfilename(title='Select Image')
    img = Image.open(selected_img)
    # ----- The code below resizes the image -------
    # ----- to 300px width keeping the original ----
    # ----- image proportions ----------------------
    basewidth = 300
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    # ----- End of resizing image ------------------
    # redraw_image = ImageDraw.Draw(img)
    # black = (3, 8, 12)
    # # font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    # redraw_image.text((0, 0), 'photopathway.com', fill=black)
    loaded_image = ImageTk.PhotoImage(img)

    # canvas.create_image(basewidth, hsize, anchor=NW, image=loaded_image)

    label1 = Label(image=loaded_image)
    label1.image = loaded_image
    label1.grid(column=0, row=3, columnspan=2)
    return(img, loaded_image)

    # img.show()


def apply_watermark():
    redraw_image = ImageDraw.Draw(img)
    black = (3, 8, 12)
    # font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    redraw_image.text((0, 0), 'photopathway.com', fill=black)
    loaded_image = ImageTk.PhotoImage(img)
    label1 = Label(image=loaded_image)
    label1.image = loaded_image
    label1.grid(column=0, row=3, columnspan=2)


# def watermark_text(input_image_path,
#                    output_image_path,
#                    text, pos):
#     photo = Image.open(input_image_path)
#     # make the image editable
#     drawing = ImageDraw.Draw(photo)
#     black = (3, 8, 12)
#     font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
#     drawing.text(pos, text, fill=black, font=font)
#     photo.show()
#     photo.save(output_image_path)


# if __name__ == '__main__':
#     img = 'lighthouse.jpg'
#     watermark_text(img, 'lighthouse_watermarked.jpg',
#                    text='www.mousevspython.com',
#                    pos=(0, 0))


window = Tk()
window.title("WaterMark.me")
window.config(padx=50, pady=50, bg=DARKGRAY)


canvas = Canvas(width=500, height=224, bg=DARKGRAY, highlightthickness=0)
canvas.grid()

title_label = Label(text="WaterMark.me", font=(
    FONT_NAME, 30, "bold"), fg=MIDNIGHTBLUE, bg=DARKGRAY)
title_label.grid(column=0, row=0)


open_image_button = Button(text="Open Image", font=(
    FONT_NAME, 10, "bold"), command=open_img, highlightthickness=0)
open_image_button.grid(column=0, row=1)

apply_watermark_button = Button(text="Apply Watermark", font=(
    FONT_NAME, 10, "bold"), command=apply_watermark, highlightthickness=0)
apply_watermark_button.grid(column=1, row=1)

save_image_button = Button(text="Save Image", font=(
    FONT_NAME, 10, "bold"), command="", highlightthickness=0)
save_image_button.grid(column=2, row=1)

watermark_text_label = Label(text="Watermark text:", bg=DARKGRAY)
watermark_text_label.grid(column=0, row=2)

watermark_text = Entry(width=35)
watermark_text.focus()
watermark_text.grid(column=1, row=2)


window.mainloop()
