"""
Authors: Katie Williams and Megan Paynton

Aim: Write functions which can shift and rotate an image to match a fixed image

"""

# First, import the relevant modules and functions
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread 
from scipy.ndimage import interpolation, rotate

# Load the file, lungs.jpg and Lungs2.jpg
lungs = imread("lungs.jpg", as_gray=True) # load the file with as_gray = T loads the file in 2 dimentions (black and white - grey scale)
#lungs2 = imread("lungs2.jpg", as_gray=True)

# Load the file lungs3.jpg, using as_gray=TRUE to reduce the number of channels to 1
lungs3 = imread("lungs3.jpg", as_gray=True) 
fig, ax = plt.subplots()

# Plot the two images, lungs.jpg and lung3.jpg, with transparency, where the Green scan is the 'fixed' image (lungs.jpg)
ax.imshow(lungs, cmap="Greens_r", alpha=0.5) 
ax.imshow(lungs3, cmap="Purples_r", alpha=0.5)
plt.title("Both CT scans, on the same Axes")
plt.show() #view the two plots on the same axis


####### Write a function to shift and rotate the floating image a specified number of shifts and degrees #######

# Two input arguments, the required shifts (defined by a list, as before) 
# and the number of degrees to shift the image clockwise (if a positive number is given), 
def transformImage(shifts, rotates):
    global lungs3
    global floating
    shifted_image = interpolation.shift(lungs3, shifts) # interpolation shifts the specified image
    transformed_image = rotate(shifted_image, -rotates, reshape=False) # rotate function rotates the shifted image a specific number of degrees, reshape=False stops the image being increased or decreased in size
    lungs3 = transformed_image
    floating.set_data(lungs3)
    fig.canvas.draw()


####### Write code to allow the image to be shifted using the arrow keys on the keyboard #######

# Create a new figure
fig, ax = plt.subplots()
fixed = ax.imshow(lungs, cmap="Greens_r", alpha=0.5)
floating = ax.imshow(lungs3, alpha=0.5, cmap="Purples_r")

up = 0
down = 0
left = 0
right = 0
cw = 0
acw = 0
# Function to shift floating image with keyboard presses
def eventHandler(event):
    global up
    global down
    global left
    global right
    global cw
    global acw
    whichKey = event.key
    if whichKey == "up":
        up += 1
        transformImage([-1,0], 0)
    elif whichKey == "down":
        down += 1
        transformImage([1,0], 0)
    elif whichKey == "right":
        right += 1
        transformImage([0,1], 0)
    elif whichKey == "left":
        left += 1
        transformImage([0,-1], 0)
    elif whichKey == ".":
        cw += 1
        transformImage([0,0], 1)
    elif whichKey == ",":
        acw += 1
        transformImage([0,0], -1)

fig.canvas.mpl_connect("key_press_event", eventHandler) # call the key press event to the figure
plt.title("Shift the Image to align using the arrow keys, and rotate using < >")
plt.show()
print(f'You moved {down-up} down and {right-left} right and rotated {cw-acw} degrees clockwise.')
