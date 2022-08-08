#reformatting image
import numpy as np
import cv2
from picamera import PiCamera
from PIL import Image
import imutils
from Cam.color_id import *

WIDTH = 1024
HEIGHT = 768

def color_id2(img):
    enImg = process(img)

    #mask
    mask_img = mask(enImg)
    folder_path = '/home/pi/BloomCube/satImage/'
    cv2.imwrite(folder_path + 'scannertest.jpg', mask_img)

    #percentages
    per = perc(mask_img)
    print(per)
    if per > 0.1: #default is 0.3 #eric: 0.1
        return True



def image_processing():
    filename = take() #take() takes image, filename now is string of file path
    img = cv2.imread(filename) #img opens the file
    #TESTING
    #img = cv2.imread('Images/all.jpg')
    #create subarray of the pixels in rows 256 to 768, and in columns 192 to 576
    newW = np.tan(6*np.pi/180) * HEIGHT
    newW = round(newW)
    cropped_img = img[0:600, (512-newW):(512+newW)]
    return color_id2(cropped_img)
