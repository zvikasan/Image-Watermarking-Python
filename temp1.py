import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont

DARKGRAY = "#A9A9A9"
DIMGRAY = "#696969"
MIDNIGHTBLUE = "#191970"

FONT_NAME = "Helvetica"


def open_img():
    global img
    global loaded_img
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
    loaded_img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 20, anchor=NW,image=loaded_img)


def apply_watermark():
    global img
    global loaded_img
    redraw_image = ImageDraw.Draw(img)
    black = (3, 8, 12)
    # font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    redraw_image.text((0, 0), 'photopathway.com', fill=black)
    loaded_img = ImageTk.PhotoImage(img)
    canvas.create_image(0, 20, anchor=NW, image=loaded_img)


def save_img():
    global img
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    img.save(filename)

window = Tk()
window.title("WaterMark.me")
window.config(padx=50, pady=50, bg=DARKGRAY)

canvas = Canvas(window, width=500, height=300, bg=DARKGRAY, highlightthickness=0)
canvas.grid(column=2, row=5)

title_label = Label(text="WaterMark. me", font=(
    FONT_NAME, 30, "bold"), fg=MIDNIGHTBLUE, bg=DARKGRAY)
title_label.grid(column=0, row=0, columnspan=3, pady=20, sticky=tk.N+tk.S+tk.W+tk.E)

open_image_button = Button(text="Open Image", font=(
    FONT_NAME, 10, "bold"), command=open_img, highlightthickness=0)
open_image_button.grid(column=0, row=1, pady=20)

apply_watermark_button = Button(text="Apply Watermark", font=(
    FONT_NAME, 10, "bold"), command=apply_watermark, highlightthickness=0)
apply_watermark_button.grid(column=1, row=1)

save_image_button = Button(text="Save Image", font=(
    FONT_NAME, 10, "bold"), command=save_img, highlightthickness=0)
save_image_button.grid(column=2, row=1)

watermark_text_label = Label(text="Watermark text:", bg=DARKGRAY)
watermark_text_label.grid(column=0, row=3)

watermark_text = Entry(width=35)
watermark_text.focus()
watermark_text.grid(column=1, row=3, sticky=tk.N+tk.S+tk.W+tk.E)

window.mainloop()

