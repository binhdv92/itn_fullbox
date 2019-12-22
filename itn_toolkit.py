# -*- coding: utf-8 -*-
# In[] Import
import argparse
import cv2
from datetime import datetime
import os


# In[]
parser = argparse.ArgumentParser()
parser.add_argument('-n','--name',default='CAP')
parser.add_argument('-p','--path',default='images')

args=parser.parse_args()

print(args.name)
print(args.path)


# In[] Declare
def get_picture_name():
    dt = datetime.now()
    dtstr=f"{dt}"
    dtstr=dtstr.replace(" ","_")
    dtstr=dtstr.replace(":","")
    dtstr=dtstr.replace("-","")
    dtstr=dtstr.replace(".","_")
    IMAGE_NAME=os.path.join(args.path, f"{args.name}_{dtstr}.jpg")
    return IMAGE_NAME

print(get_picture_name())


# In[]
cap = cv2.VideoCapture(0) 

   
while True:
    ret,frame = cap.read()
    frame = cv2.rotate(frame,cv2.ROTATE_180)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cv2.imshow("Frame",frame)

    key = cv2.waitKey(1)
    
    if key == ord("q"):
        print("exit programe")
        break
    elif(key == ord("s")):
        IMAGE_NAME=get_picture_name()
        print(f"Save {IMAGE_NAME} to disk")
        cv2.imwrite(IMAGE_NAME,frame)


# Close device
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()

#!exit

