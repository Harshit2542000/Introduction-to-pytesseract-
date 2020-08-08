# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 13:12:31 2020

@author: harshit
"""
#using tesseract engine for windows to get the characters from text
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd='C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
img=cv2.imread('1.png')
#converting the image to the rgb as tesseract expects an rgb image in it and opencv extracts image in bgr format by default
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#print(pytesseract.pytesseract.image_to_string(img))
#detecting the bounding box for each of the characters
#print(pytesseract.pytesseract.image_to_boxes(img))
#detecting characters
'''himg,wimg,_=img.shape
cong=r'--oem 3 --psm 6 outputbase digits'
boxes=pytesseract.pytesseract.image_to_boxes(img,config=cong)
for box in boxes.splitlines():
    #print(box)
    box=box.split(" ")
    #print(box)
    x,y,w,h=int(box[1]),int(box[2]),int(box[3]),int(box[4])
    cv2.rectangle(img,(x,himg-y),(w,himg-h),(0,0,255),3)
    cv2.putText(img,box[0],(x,himg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
cv2.imshow("Result",img)
cv2.waitKey(0)'''
#capturing the words
hword,wword,_=img.shape
cong=r'--oem 3 --psm 6 outputbase digits'
boxesword=pytesseract.image_to_data(img,config=cong)
for x,boxword in enumerate(boxesword.splitlines()):
    boxword=boxword.split()
    #print(boxword)
    if(len(boxword)==12):
        if x!=0:
            xword,yword,wword1,hword=int(boxword[6]),int(boxword[7]),int(boxword[8]),int(boxword[9])
            cv2.rectangle(img,(xword,yword),(xword+wword1,yword+hword),(0,0,255),3)
            cv2.putText(img,boxword[11],(xword,yword),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
cv2.imshow("Words",img)
cv2.waitKey(0)        