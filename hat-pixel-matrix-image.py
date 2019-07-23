#!/usr/bin/env python 
# this script will show a matrix of colors on the Pi HAT 
from sense_hat import SenseHat
sense = SenseHat()
r = (255, 0, 0)
b = (0, 0, 255)

w = (255, 255, 255)

pixeld = [
    b, b, b, b, r, r, r, r,    
    b, b, b, b, r, r, r, r,    
    b, b, b, b, r, r, r, r, 
    b, b, b, b, r, r, r, r, 
    b, b, b, b, r, r, r, r, 
    b, b, b, b, r, r, r, r, 
    b, b, b, b, r, r, r, r, 
    b, b, b, b, r, r, r, r, 
]
sense.set_pixels(pixels)
