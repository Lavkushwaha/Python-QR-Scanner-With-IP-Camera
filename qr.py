import numpy as np
import cv2
from PIL import Image
from pyzbar.pyzbar import decode
import time

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('rtsp://192.168.43.1:8080/h264_ulaw.sdp')

while(True):

    # ret, frame = cap.read()
    ret, frame = cap.read()


    cv2.imshow('frame',frame)
   
    x = input("Ready Press Y if Yes :")
    if x == 'Y' or x == 'y':
       
        return_value, image = cap.read() 
        # cv2.imshow('image',image)

        # image.save('img.png')
        cv2.imwrite('img.png',image)
        time.sleep(1.5)
        res = decode(Image.open('img.png'))
        idata = res[0].data
        print(str(idata))
        break

    if x == 'n' or x == 'N':
        exit()


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

