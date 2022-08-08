#Name: Team Cam-1 (Evelyn)
#Date: 07/14/2022

import time
from time import sleep
import os
import board
import math
import busio
import adafruit_fxos8700
from git import Repo
from picamera import PiCamera
from tkinter import *


#i2c = busio.I2C(board.SCL, board.SDA)
#sensor = adafruit_fxos8700.FXOS8700(i2c)
camera = PiCamera()
camera.resolution = (1024, 768)
effectlist = ["none", "negative", "solarize", "sketch", "denoise", 
    "emboss", "oilpaint", "hatch", "gpen", "pastel", "watercolor",
    "film", "blur", "saturation", "colorswap", "washedout", "posterise", 
    "colorpoint", "colorbalance", "cartoon", "deinterlace1", "deinterlace2"]

"""
Names files according to which effect and level of that effect
that is being tested. If inputs are not strings, an assertion
error will be raised

Args:
    sett: string representing the folder that the file saves into
    typ: string representing the file name

Returns:
    File name of the tested effect. 

Raises:
    AssertionError when sett or typ is not a string
"""
def name(sett, typ):
    assert type(sett) is str and type(typ) is str
    filen = "/home/pi/cam-1/CritFunc/04Images/" + sett.lower() + "/" + typ + ".jpg"
    return filen

"""
Uses the camera to take a picture by changing the effects settings. 
If input is not a string or not in the list of viable inputs, an 
assertion error will be raised. 

Args:
    effect: string representing image effect option chosen by the
    user

Returns:
    String signifying that the picture has been taken. 

Raises:
    AssertionError: raised when effect is not a string or when
    effect is not in the list of viable effects. 
"""
def effects(effect):
    assert type(effect) is str and effect in effectlist 
    yayornay = input("Ready to take a picture? Yes or No?\n")
    if yayornay == "Yes":
        camera.image_effect = effect
        camera.capture(name("effects", effect))
        sleep(1)
        return "Finished taking effect photo!"
    return "Did not take photos"

"""
Uses the camera to take a picture by changing the annotation
settings. If input is not a string, an assertion error will 
be raised. 

Args:
    text: string representing desired annotation given by the user
    input.

Returns:
    String signifying that the picture has been taken. 

Raises:
    AssertionError: raised when text is not a string. 
"""
def texts(text):
    assert type(text) is str
    yayornay = input("Ready to take a picture? Yes or No?\n")
    if yayornay == "Yes":
        camera.annotate_text = text
        camera.capture(name("text", text[0:3]))
        sleep(1)
        return "Finished taking text photo!"
    return "Did not take photos"

"""
Uses the camera to take a picture by changing the contrast settings. 
If input is not an integer, an assertion error will be raised. 

Args:
    lvl: integer representing the level of contrast desired by the
    user input

Returns:
    String signifying that the picture has been taken. 

Raises:
    AssertionError: raised when the contrast level is not an integer
    or between 0 and 100 
"""
def contrast(lvl):
    assert type(lvl) is int and lvl >= 0 and lvl <= 100
    yayornay = input("Ready to take a picture? Yes or No?\n")
    if yayornay == "Yes":
        camera.annotate_text = "Contrast: " + str(lvl)
        camera.contrast = lvl
        camera.capture(name("contrast", "con" + str(lvl)))
        sleep(1)
        return "Finished taking contrast photo!"
    return "Did not take photos"

#Runs the program
def main():
    l = ["Effects", "Texts", "Contrast"]
    print(l)
    setting = input("Choose one of the above\n")
    if setting == l[0]:
        print(effectlist)
        typ = input("Choose one of the above\n")
        print(effects(typ))
    elif setting == l[1]:
        tex = input("What annotation?\n")
        print(texts(str(tex)))
    elif setting == l[2]:
        level = input("What level of contrast?")
        print(contrast(int(level)))
    else:
        print("Entered in wrong. Try again.")
    

if __name__ == "__main__":
    main()