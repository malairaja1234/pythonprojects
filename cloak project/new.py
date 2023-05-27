from tkinter import *
from tkinter import *
from datetime import date
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import os
import numpy as np
import cv2
import time

def display_gif_animation(gif_path, root):
    def update_animation(frame):
        # Get the next frame from the GIF
        gif_image.seek(frame)
        # Convert the GIF frame to Tkinter-compatible format
        tk_image = ImageTk.PhotoImage(gif_image)
        # Update the label with the new frame
        label.config(image=tk_image)
        label.image = tk_image
        # Schedule the next frame update after a delay (in milliseconds)
        root.after(delay, update_animation, frame + 1)

    # Load the GIF image
    gif_image = Image.open(gif_path)

    # Create a label to display the GIF
    label = Label(root)
    label.pack()

    # Set the initial frame to display
    initial_frame = 0

    # Set the delay between frames (in milliseconds)
    delay = gif_image.info['duration']

    # Start the animation update process
    update_animation(initial_frame)

def invisible():
    # Your existing code for the invisible function goes here
    # ...
    cap = cv2.VideoCapture(0)
    time.sleep(2)     
    background = 0
    for i in range(50):
        ret, background = cap.read()
    while(cap.isOpened()): 
        ret, img = cap.read()
        if not ret:
            break
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        lower_red = np.array([0,120,70])
        upper_red = np.array([10,255,255]) # values is for red colour Cloth
        mask1 = cv2.inRange(hsv, lower_red,upper_red)
        lower_red = np.array([170,120,70])
        upper_red =  np.array([180,255,255])
        mask2 = cv2.inRange(hsv,lower_red,upper_red)
        mask1 = mask1 +mask2
        mask1 = cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.uint8), iterations = 2)
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE,np.ones((3,3),np.uint8), iterations = 1)

        mask2 =cv2.bitwise_not(mask1)
        res1 = cv2.bitwise_and(background,background,mask=mask1)
        res2 = cv2.bitwise_and(img,img,mask=mask2)
        final_output = cv2.addWeighted(res1,1,res2,1,0)
        cv2.imshow('Invisible Cloak',final_output)
        k = cv2.waitKey(10)
        if k==27:
            break
    cap.release()
    cv2.destroyAllWindows()



background = "#062830"

root = Tk()
root.title("student registration")
root.geometry("1250x700+210+100")
root.config(bg=background)

Label(root, text="Email: malairaja10108@gmail.com", width=30, height=2, bg="blue", anchor='e').pack(side=TOP, fill=X)
Label(root, text="Invisible Cloak using OpenCV", width=30, height=2, bg="brown", fg="white", font="arial 20 bold").pack(side=TOP, fill=X)


Label(root, text="Click Esc to escape", width=30, height=2,fg="green",bg=background, font="arial 12 bold").place(x=560,y=500)

Srch = Button(root, text="Expecto Patronum", width=20, height=1, bg="grey", fg="white", font="arial 13 bold", command=invisible).place(x=580, y=558)

# Display the GIF animation
display_gif_animation("harry.gif", root)


root.mainloop()
