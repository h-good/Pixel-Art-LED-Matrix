from PIL import Image
#import numpy as np
import board
import neopixel
import time
import os
import random

LED_mat = neopixel.NeoPixel(board.D18, 576, auto_write = False, pixel_order="BRG", brightness = 0.25)

try:
    while(1):
        I_str = random.choice(os.listdir("/home/pi/Documents/Python/pixel_art_pics"))
        # Begin if animated
        if I_str.find('@') != -1:
            endIndex = I_str.find('@')
            base_str = I_str[0:endIndex:1]
            animation1 = "/home/pi/Documents/Python/pixel_art_pics/" + base_str + "1@.JPG"
            animation2 = "/home/pi/Documents/Python/pixel_art_pics/" + base_str + "2@.JPG"
            for l in range(10):
                if l % 2 == 0:
                    I = Image.open(animation1)
                else:
                    I = Image.open(animation2)
                new_size = (18, 32)
                # resize image
                I2 = I.resize(new_size)
                pixels = I2.load()
                try:
                    j = 0
                    for i in range(32):
                        if i % 2 == 0:
                            try:
                                for k in range(18):
                                    if k == 0:
                                        LED_mat[j] = pixels[k, i]
                                    else:
                                        LED_mat[j] = pixels[k, i]
                                    j = j + 1
                            except:
                                pass
                        if i % 2 == 1:
                            try:
                                for l in range(18):
                                    if j % 18 == 17:
                                        pass
                                    else:
                                        LED_mat[j] = pixels[18-3-l, i]
                                    j = j + 1
                            except:
                                pass
                except:
                    pass
                LED_mat.show()
                time.sleep(.25)
#End if animated
                            
        I = Image.open("/home/pi/Documents/Python/pixel_art_pics/" +I_str)
        

        # Maintain aspect ratio while also maximizing use of display
#         w_org, h_org = I.size
#         w_percent = 18/w_org
#         h_percent = 32/h_org

        #Scale by the smaller of the percentages
#         scale_percent = min(w_percent, h_percent)
#         w_new = int(scale_percent*w_org)
#         h_new = int(scale_percent*h_org)

#         new_size = (w_new, h_new)
        new_size = (18, 32)
        # resize image
        I2 = I.resize(new_size)
        pixels = I2.load()
        try:
            j = 0
            for i in range(32):
                if i % 2 == 0:
                    try:
                        for k in range(18):
                            if k == 0:
                                LED_mat[j] = pixels[k, i]
                            else:
                                LED_mat[j] = pixels[k, i]
                            j = j + 1
                    except:
                        pass
                if i % 2 == 1:
                    try:
                        for l in range(18):
                            if j % 18 == 17:
                                pass
                            else:
                                LED_mat[j] = pixels[18-3-l, i]
                            j = j + 1
                    except:
                        pass
        except:
            pass
        LED_mat.show()
        time.sleep(4)
except KeyboardInterrupt:
    pass
