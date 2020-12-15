#-*-coding: utf-8 -*-
import cv2
import numpy as np
from cv2 import boundingRect, countNonZero, cvtColor, drawContours, findContours, getStructuringElement, imread, morphologyEx, pyrDown, rectangle, threshold
from PIL import Image
import os
from pytesseract import *

str_list = []
fn = open('/home/pi/Downloads/tomcat9/webapps/ROOT/filename.txt', 'r')
fname = fn.read()
fn.close()
large = cv2.imread("/home/pi/Downloads/tomcat9/webapps/ROOT/"+fname)
# downsample and use it for processing
rgb = large
rgb1 = large

# apply grayscale
small = cvtColor(rgb, cv2.COLOR_BGR2GRAY)
# morphological gradient
morph_kernel = getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
grad = morphologyEx(small, cv2.MORPH_GRADIENT, morph_kernel)
# binarize
#dilation = morphologyEx(grad, cv2.MORPH_CLOSE, morph_kernel)
_, bw = threshold(src=grad, thresh=0, maxval=255, type=cv2.THRESH_BINARY+cv2.THRESH_OTSU)
dilate = cv2.dilate(bw, morph_kernel, iterations = 5)

#Image.fromarray(dilate).show()
morph_kernel = getStructuringElement(cv2.MORPH_RECT, (9, 1))
#작은 구멍을 메우고 경계를 강화
connected = morphologyEx(dilate, cv2.MORPH_CLOSE, morph_kernel)

#Image.fromarray(connected).show()
mask = np.zeros(bw.shape)
# find contours
_,contours, hierarchy = findContours(connected, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
# filter contours
for idx in range(len(contours)):
    x, y, w, h = cv2.boundingRect(contours[idx])
    mask[y:y+h, x:x+w] = 0
    cv2.drawContours(mask, contours, idx, (255, 255, 255), -1)
    r = float(cv2.countNonZero(mask[y:y+h, x:x+w])) / (w * h)

    if r > 0.45 and w > 15 and h > 15:
         
         rgb = cv2.rectangle(rgb, (x, y+h), (x+w, y), (0,255,0),3)
         #Image.fromarray(rgb).show()
         #img = imread(r"C:\Users\hong\Desktop\q1.jpg")
         crop = rgb1[y:y+h+3,x:x+w+3]
         str_list.append(crop)
         #Image.fromarray(crop).show()
         #cv2.imshow("d",crop)
        # cv2.waitKey(0)
         #cv2.destroyAllWindows()
         #text = image_to_string(crop, lang="kor+eng")

         #with open("ST1.hwp", "a+") as f:
          #   f.write(text)

Image.fromarray(rgb).show()
k=list()
for i in range(len(str_list),0,-1):
    k.append(image_to_string(str_list[i-1], lang="kor+eng"))
f=open('/home/pi/Downloads/tomcat9/webapps/ROOT/convert.hwp','w')
for text in k:
    f.write(text[:len(text)-1])


#    str += texts
#l=s.splitlines()
#for i in l:
#    if i=='':
#        continue
#    f.write(i+'\n')
#    print(i)

#print(l)
#with open("ST2.hwp", "w") as f:
#    f.write(str)         
# write original image with added contours to disk  
f.close()
