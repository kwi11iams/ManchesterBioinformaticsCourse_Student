# -*- coding: utf-8 -*-
"""
Assignment Part 1
Naomi/Ali/Keith
The #%% allowed me to run it as a cell (similar to jupyter notebook) and
see it the final graphs in a tab in VScode, wont cause any problem if you delete/if it causes issues
for you.
"""

#%%
#Import necessary modules
import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread
from scipy import ndimage
from scipy.ndimage import interpolation
from scipy.ndimage import rotate

#Load images lungs.jpg, lungs2.jpg, lungs3.jpg
folder_input = '/home/ali/git_repos/ICT_module/ManchesterBioinformaticsCourse_Student/Day3/Code/'
lungs_image = np.mean(imread(folder_input + 'lungs.jpg'), -1)
lungs_image_2 = np.mean(imread(folder_input + 'lungs2.jpg'), -1)
lungs_image_3 = np.mean(imread(folder_input + 'lungs3.jpg'), -1)

fig = plt.figure() #set up a figure space, I had to take this out the function to be able to call it outside of the function
ax = fig.add_subplot(111) #add subplots for each thing - images and histogram
ax.imshow(lungs_image, cmap="Greys_r")  #designates the static image on the plot
floating = ax.imshow(lungs_image_3, cmap="Greys_r", alpha = 0.5) # and designates the floating image, alpha shows transparency level

#Co-orindates come in a small list this function takes a horizontal and vertical co-oridnate
def shiftimage(coordinate_list):
    global lungs_image_3 #changes we make to this image inside the function have an effect outside the function too
    Vertical = coordinate_list[0] #takes the vertical co-ordinate value from the input list
    Horizontal = coordinate_list[1] #takes the horizontl co-ordinate value from the input list
    Rotational = coordinate_list[2] #takes the rotational co-ordinate from the list
    xy_shift = interpolation.shift(lungs_image_3, (Vertical, Horizontal), mode="nearest") #shifts the image on the x,y as per the input co-ordinates
    rotation_shift = ndimage.rotate(xy_shift, Rotational, reshape=False)#rotates as per the input co-ordinates, reshape stops it squashing the image
    lungs_image_3 = rotation_shift #Changes the lungs_image_3 variable as per the above changes
    floating.set_data(lungs_image_3) # updates figure axis
    fig.canvas.draw() #updates figure if displayed

###Moving checks need to double check inputs (I got frustrated and messed around with them)
#lung_1_and_2_overlay = shiftimage([-18,-33, 0]) ###CHECK These input shifts should roughly level the top and bottom images
#lung_1_and_3_overlay = shiftimage([-18,33, -3]) ###CHECK these input shifts should roughly level the top and bottom images

def eventHandler(event):
    #This function handles deciphering what the user wants us to do, the event knows whichkey has been pressed.
    ###Just need to add more elif for the others hopefully
    up = 0
    down = 1
    whichKey = event.key
    if whichKey == 'up': #Takes the up keystroke and calls the shiftimage function to move it up
        up = 1
        shiftimage([-1,0,0])
        print('up') 
    elif whichKey == 'down': #Takes the down keystroke and calls the shiftimage function to move it down
        shiftimage([1,0,0])
        print('down')
    elif whichKey == 'right': #Takes the right keystroke and calls the shiftimage function to move it right 
        shiftimage([0,1,0])
        print('right')
    elif whichKey == 'left': #Takes the left keystroke and calls the shiftimage function to move it left
        shiftimage([0,-1,0])
        print('left')
    elif whichKey == 'c': #Takes the c keystroke and calls the shiftimage function to move it clockwise
        shiftimage([0,0,-1])
        print('clockwise')
    elif whichKey == 'a': #Takes the a keystroke and calls the shiftimage function to move it anticlockwise
        shiftimage([0,0,1])
        print('anticlockwise')
    
    
fig.canvas.mpl_connect('key_press_event', eventHandler) #connects the two functions so you can manipulate the image with keystrokes
plt.show()



# %%
