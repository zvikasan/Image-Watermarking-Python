# This code allows user to load an image, apply watermark to it, and save new image with the watermark.
# Watermark can be either custom text, custom image or both.
# The image displayed in the window is resized (maintaining the correct proportions) just for viewing purposes.
# When user saves the image - the original image is saved.

#Note: There was no emphasis here on the program interface design, but just on the functionality

from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw, ImageFont

MIDNIGHTBLUE = "#191970"

FONT1 = ImageFont.truetype('Oxygen-Bold.ttf', 10)
FONT2 = "Helvetica"


def open_img():
    global img  # original image
    global display_img
    global resized_img  # reduced dimensions image to display on screen
    global basewidth
    global hsize
    global wpercent
    global selected_img

    selected_img = filedialog.askopenfilename(title='Select Image')
    img = Image.open(selected_img)
    # ----- The code below resizes the image -------
    # ----- to 300px width keeping the original ----
    # ----- image proportions ----------------------
    basewidth = 300
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    resized_img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    # ----- End of resizing image ------------------
    display_img = ImageTk.PhotoImage(resized_img)
    print(resized_img.size[0])
    print(resized_img.size[1])
    canvas.create_image(0, 20, anchor=NW, image=display_img)


def apply_watermark():
    global img
    global resized_img
    global display_img

    redraw_img = ImageDraw.Draw(img)
    redraw_resized_img = ImageDraw.Draw(resized_img)

    # text = "© photopathway.com"
    if watermark_text.get() == "":
        text = 'This is my image'
    else:
        text = watermark_text.get()

    text_size_rw = redraw_resized_img.textsize(
        text, (ImageFont.truetype('Oxygen-Bold.ttf', 10)))

    text_size = redraw_img.textsize(
        text, (ImageFont.truetype('Oxygen-Bold.ttf', int(10/wpercent))))

    redraw_img.text(
        (img.size[0] - (text_size[0]+int(10/wpercent)), img.size[1]-int(20/wpercent)), text, font=(ImageFont.truetype('Oxygen-Bold.ttf', int(10/wpercent))), color='#000000')

    redraw_resized_img.text(
        (300 - (text_size_rw[0]+10), hsize-20), text, color='#000000', font=FONT1)

    display_img = ImageTk.PhotoImage(resized_img)
    canvas.create_image(0, 20, anchor=NW, image=display_img)


def save_img():
    global img
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    img.save(filename)


def clear_watermark():    
   global img 
   global display_img
   global resized_img 

   img = Image.open(selected_img)
   basewidth = 300
   wpercent = (basewidth/float(img.size[0]))
   hsize = int((float(img.size[1])*float(wpercent)))
   resized_img = img.resize((basewidth, hsize), Image.ANTIALIAS)
   # ----- End of resizing image ------------------
   display_img = ImageTk.PhotoImage(resized_img)
   canvas.create_image(0, 20, anchor=NW, image=display_img)

def open_watermark_image():
    global img
    global resized_img
    global display_img


    w_img = filedialog.askopenfilename(title='Select Image')
    watermark_img = Image.open(w_img)
    watermark_img.putalpha(100)
    # ----- The code below resizes the image -------
    # ----- to 300px width keeping the original ----
    # ----- image proportions ----------------------
    basewidth_w = 100
    wpercent_w = (basewidth_w/float(watermark_img.size[0]))
    hsize_w = int((float(watermark_img.size[1])*float(wpercent_w)))
    resized_wimg = watermark_img.resize((basewidth_w, hsize_w), Image.ANTIALIAS)
    # ----- End of resizing image ------------------
    display_wimg = ImageTk.PhotoImage(resized_wimg)
    
    position_large = int(img.width/2 - watermark_img.width/2), int(img.height/2 - watermark_img.height/2)
    
    position_small = int(resized_img.width/2 - resized_wimg.width/2), int(resized_img.height/2 - resized_wimg.height/2)

    img.paste(watermark_img, position_large, watermark_img)
    resized_img.paste(resized_wimg, position_small, resized_wimg)

    display_img = ImageTk.PhotoImage(resized_img)
    canvas.create_image(0, 20, anchor=NW, image=display_img)
    

window = Tk()
window.title("WaterMark.me")
window.minsize(width=600, height=850)
window.config(bg='white')

frame = Frame(window, bg='#d3e0fa', bd=0.03)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)


title_label = Label(frame, text="WaterMark. me", font=(
    FONT2, 30, "bold"), fg=MIDNIGHTBLUE, bg='white')
title_label.place(relx=0, rely=0.04, relwidth=0.8, relheight=0.1)

open_image_button = Button(frame, text="Open Image", font=(
    FONT2, 10, "bold"), command=open_img, highlightthickness=0)
open_image_button.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.07)   

open_watermark_image = Button(frame, text="Open Watermark Image", font=(
    FONT2, 10, "bold"), command=open_watermark_image, highlightthickness=0)
open_watermark_image.place(relx=0.32, rely=0.2, relwidth=0.35, relheight=0.07)

save_image_button = Button(frame, text="Save Image", font=(
    FONT2, 10, "bold"), command=save_img, highlightthickness=0)
save_image_button.place(relx=0.69, rely=0.2, relwidth=0.2, relheight=0.07)

watermark_text_label = Label(frame, text="Watermark text:")
watermark_text_label.place(relx=0.1, rely=0.3, relwidth=0.2, relheight=0.07)

watermark_text = Entry(frame, width=35)
watermark_text.focus()
watermark_text.place(relx=0.32, rely=0.3, relwidth=0.57, relheight=0.07)

apply_watermark_button = Button(frame, text="Apply Watermark Text", font=(
    FONT2, 10, "bold"), command=apply_watermark, highlightthickness=0)
apply_watermark_button.place(relx=0.1, rely=0.4, relwidth=0.4, relheight=0.07)

clear_watermark_button = Button(frame, text="Clear Watermark", font=(
    FONT2, 10, "bold"), command=clear_watermark, highlightthickness=0)
clear_watermark_button.place(relx=0.52, rely=0.4, relwidth=0.37, relheight=0.07)


canvas = Canvas(frame, width=300, height=400,
                bg='#d3e0fa', highlightthickness=0)
canvas.place(relx=0.2, rely=0.5)

quit_button = Button(frame, text='Exit', font=(
    FONT2, 10, "bold"), command=window.destroy)
quit_button.place(relx=0.85, rely=0.9, relwidth=0.1, relheight=0.05)

window.mainloop()
