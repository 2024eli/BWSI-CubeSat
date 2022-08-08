#Evelyn Li
#BloomCube
#07/28/2022

import cv2
import numpy as np
from picamera import PiCamera
import matplotlib.pyplot as plt
import imutils

MM2_TO_PX = 279.8214 / 3923.5
color_range = {}
#color_range["red"] = [(155, 55, 55), (179, 255, 255)] #neil's
#color_range["red"] = [(150,25, 25), (179, 255, 255)] #ours
color_range["red"] = [(155,55,55), (179, 255, 255)] #eric

#function to increase contrast to tell red
def process(img):
    #print(img)
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

def contour(img):
    hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask = cv2.inRange(hsvImg, *color_range["red"])
    edged = cv2.Canny(gray, 30, 200)
    cnts = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    total_a = 0.0
    total_p = 0.0
    for c in cnts:
        area = cv2.contourArea(c)
        if (area < 5):
            continue
        total_a += area
        total_p += cv2.arcLength(c,True)
        cv2.drawContours(img, [c], -1, (0, 255, 0), 3)
    
    non = cv2.countNonZero(mask)
    print("NonZero Area: ", non)
    #print("Contour Area: ", total_a)
    #print("Contour Peri: ", total_p)
    
    cv2.destroyAllWindows()
    return img, non

def calc(area):
    return area * MM2_TO_PX

def area_calc(img):
    #make red more red
    folder_path = '/home/pi/BloomCube/ReceiveImages'
    image = cv2.imread('/home/pi/BloomCube/ReceiveImages/' + img)
    enImg = process(image)
    enPath = 'enImage.jpg'
    cv2.imwrite(folder_path + '/' + enPath, enImg)
    print('Enhanced image saved')

    #mask
    mask_image = cv2.imread('ReceiveImages/' + enPath)
    mask_img = mask(mask_image)
    mPath = 'mask_' + img
    cv2.imwrite(folder_path + '/mask_' + img, mask_img)
    print('Mask image saved')

    #contour
    con = cv2.imread('ReceiveImages/' + mPath)
    con_image, area = contour(con)
    cPath = 'con_' + img
    cv2.imwrite(folder_path + '/' + cPath, con_image)
    print('Contour image saved')

    #calc
    ar = calc(area)
    print("Area in mm2 is: ", ar, "mm2")
    return ar


if __name__ == '__main__':
    import sys
    area_calc(*sys.argv[1:])