from PIL import Image
#import numpy as np
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
options.gpio_slowdown = 4
# options.chain_length = 1
# options.parallel = 1
options.hardware_mapping = 'adafruit-hat'  # If you have an Adafruit HAT: 'adafruit-hat'

matrix = RGBMatrix(options = options)

I = Image.open("C19.JPG")
newSize = [32, 64]
I = I.resize(newSize)
pix = I.load()
for i in range(64):
    for j in range(32):
        matrix.SetPixel(i,j,pix[j,i][0],pix[j,i][1],pix[j,i][2])

# matrix.SetPixel()
                        
# I.thumbnail((matrix.width, matrix.height))
# I = Image.Image.rotate(I, 270)

# new_size = (32, 64)
# resize image
# I2 = I.resize(new_size)



# matrix.SetImage(I.convert('RGB'))


try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)

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