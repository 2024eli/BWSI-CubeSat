#Evelyn Li
#BloomCube
#07/28/2022

import cv2
import numpy as np
from picamera import PiCamera
import matplotlib.pyplot as plt
import imutils

color_range = {}
#color_range["red"] = [(155, 55, 55), (179, 255, 255)] #neil's
#color_range["red"] = [(150,25, 25), (179, 255, 255)] #ours
color_range["red"] = [(155,55,55), (179, 255, 255)] #eric

def take():
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    camera.capture('/home/pi/BloomCube/satImage/red.jpg')
    camera.stop_preview()
    camera.close()
    return '/home/pi/BloomCube/satImage/red.jpg'

#function to increase contrast to tell red
def process(img):
    hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #Edit saturation
    hsvImg[...,1] = hsvImg[...,1]*1.5
    #Edit brightness 
    hsvImg[...,2] = hsvImg[...,2]*1
    enImg=cv2.cvtColor(hsvImg,cv2.COLOR_HSV2BGR)
    return enImg

def mask(img):
    hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsvImg, *color_range["red"])
    mask = cv2.bitwise_and(img, img, mask=thresh)
    return cv2.bitwise_and(img, mask)

def perc(img):
    #TODO
    hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    thresh = cv2.inRange(hsvImg, *color_range["red"])
    red = cv2.countNonZero(thresh)
    total_pixels = 1024*768
    per = red/total_pixels
    return round(100*per, 2)

def color_id(img = 'red.jpg'):
    #make red more red
    folder_path = '/home/pi/BloomCube/satImage/'
    image = cv2.imread(folder_path + img)
    enImg = process(image)

    #mask
    mask_img = mask(enImg)
    cv2.imwrite(folder_path + 'mask.jpg', mask_img)

    per = perc(mask_img) 
    if per > 20:
        return True


if __name__ == '__main__':
    import sys
    color_id(*sys.argv[1:])
