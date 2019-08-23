import cv2
import numpy as np

from PIL import Image
from pyzbar.pyzbar import decode
import time


f= open("bmsdata.txt","a+")

#print("Before URL")
# cap = cv2.VideoCapture('rtsp://192.168.43.1:8080/h264_ulaw.sdp')
#print("After URL")

while True:

    #print('About to start the Read command')
    # ret, frame = cap.read()
    #print('About to show frame of Video.')
    
    # cv2.imshow("Capturing",frame)

    x = input("Ready Press Y if Yes :")
    if x == 'Y' or x == 'y':   
        # return_value, image = cap.read() 
        # cv2.imwrite('img.png',image)
        # time.sleep(1.5)

        res = decode(Image.open('BMS10666.png'))
        idata = res[0].data
        qrdata = str(idata)[2:-1].split('?',2)
        print("BMSID :",qrdata[1])
        f.write("\n BMSid : {}".format(qrdata[1]) )
        break


    #print('Running..')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cap.release()
# cv2.destroyAllWindows()