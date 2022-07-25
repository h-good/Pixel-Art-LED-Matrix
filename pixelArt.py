from PIL import Image
import sys
import numpy as np
#import board
#import neopixel
#from PIL import ImageDraw
from rgbmatrix import RGBMatrix, RGBMatrixOptions
import time
import os
import random

# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 32
options.cols = 64
options.gpio_slowdown = 5
# options.chain_length = 1
# options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'
matrix = RGBMatrix(options = options)

# Set the threshold value 0-255, to remove very faint pixels 
threshold = 20

# List and counter to reduce dupilcate image shows
I_str_list = ['','','','','','','','','','']
ele_ctn = 0

while(1):
    try:
        #Ensure next image has not been seen for last 10 shows
        new_I = 0
        while not new_I:
            #Get a random file
            I_str = random.choice(os.listdir("/home/pi/Documents/Python/pixel_art_pics"))
            #Check if file has appeared in the last ten image iterations, if found a new random file will be chosen
            for s in I_str_list:
                if I_str != s:
                    new_I = 1
        #Add current file name to list of shown files
        I_str_list[ele_ctn] = I_str
        if ele_ctn != 9:
            ele_ctn = ele_ctn + 1
        else:
            ele_ctn = 0
        #Open file
        I = Image.open("/home/pi/Documents/Python/pixel_art_pics/" +I_str)
        #resize image
        newSize = [32, 64]
        I = I.resize(newSize)
        # gray scale threshold the image
        Igray = I.point(lambda p: p > threshold and 255) 
        pix = I.load()
        pix_gray = Igray.load()
        for i in range(64):
            for j in range(32):
                #if pixel in threshold image is black, write pixel to black
                if pix_gray[j,i][0] == 0 and pix_gray[j,i][1] == 0 and pix_gray[j,i][2] == 0:
                    matrix.SetPixel(i,j,0,0,0)
                else:
                    matrix.SetPixel(i,j,pix[j,i][0],pix[j,i][1],pix[j,i][2])
        time.sleep(10)

    except KeyboardInterrupt:
        sys.exit(0)
# matrix.SetPixel()
                        
# I.thumbnail((matrix.width, matrix.height))
# I = Image.Image.rotate(I, 270)

# new_size = (32, 64)
# resize image
# I2 = I.resize(new_size)



# matrix.SetImage(I.convert('RGB'))




#                             
#         I = Image.open("/home/pi/Documents/Python/pixel_art_pics/" +I_str)
#         
#         new_size = (18, 32)
#         # resize image
#         I2 = I.resize(new_size)
#         pixels = I2.load()
#         try:
#             j = 0
#             for i in range(32):
#                 if i % 2 == 0:
#                     try:
#                         for k in range(18):
#                             if k == 0:
#                                 LED_mat[j] = pixels[k, i]
#                             else:
#                                 LED_mat[j] = pixels[k, i]
#                             j = j + 1
#                     except:
#                         pass
#                 if i % 2 == 1:
#                     try:
#                         for l in range(18):
#                             if j % 18 == 17:
#                                 pass
#                             else:
#                                 LED_mat[j] = pixels[18-3-l, i]
#                             j = j + 1
#                     except:
#                         pass
#         except:
#             pass
#         LED_mat.show()
#         time.sleep(4)
# except KeyboardInterrupt:
#     pass
# 