import cv2 
import numpy as np


def empty():
    pass

def getCounters(img):
    countours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in countours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(imgResult, cnt, -1, (255,0,0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            objCor = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w//2, y 
        
MyPoints = []
def drawOnCanvas(myPoints, myColor, myImage):
    for point in myPoints:
        cv2.circle(myImage, (point[0], point[1]), 10, myColor, cv2.FILLED )
            
myColors = (233,103,19)


winName="TrackBars"
cv2.namedWindow(winName)
cv2.resizeWindow(winName, 500, 250)



h_min, h_max, sat_min, sat_max, val_min, val_max = (0,0,0,0,0,0)

cv2.createTrackbar("Hue Min", winName, 0,179,empty)
cv2.createTrackbar("Hue Max", winName, 0,179,empty)
cv2.createTrackbar("Sat Min", winName, 0,255,empty)
cv2.createTrackbar("Sat Max", winName, 0,255,empty)
cv2.createTrackbar("Val Min", winName, 0,255,empty)
cv2.createTrackbar("Val Max", winName, 0,255,empty)

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    
    h_min = cv2.getTrackbarPos("Hue Min", winName)
    h_max = cv2.getTrackbarPos("Hue Max", winName)
    sat_min = cv2.getTrackbarPos("Sat Min", winName)
    sat_max = cv2.getTrackbarPos("Sat Max", winName)
    val_min = cv2.getTrackbarPos("Val Min", winName)
    val_max = cv2.getTrackbarPos("Val Max", winName)
    
    cv2.setTrackbarPos("Hue Min", winName, 99 )
    cv2.setTrackbarPos("Hue Max", winName, 179 )
    cv2.setTrackbarPos("Sat Min", winName, 155)
    cv2.setTrackbarPos("Sat Max", winName, 255)
    cv2.setTrackbarPos("Val Min", winName, 97)
    cv2.setTrackbarPos("Val Max", winName, 255)
    
    
    mins = np.array([h_min, sat_min, val_min]) 
    maxs = np.array([h_max, sat_max, val_max])
    
    mask = cv2.inRange(imgHSV, lowerb=mins, upperb=maxs)
    
 
    imgResult = cv2.bitwise_and(img, img, mask=mask)
    
    x, y = getCounters(mask)
    cv2.circle(imgResult,(x,y), 1, myColors, 10,cv2.FILLED)
    cv2.circle(img, (x,y), 1, myColors, 10, cv2.FILLED)
    
    if x != 0 and y != 0:
        MyPoints.append([x,y])
    # cv2.imshow("Camera", imgHSV)
    drawOnCanvas(myPoints=MyPoints, myColor=myColors, myImage=imgResult)
    drawOnCanvas(myPoints=MyPoints, myColor=myColors, myImage=img)
    
    
    cv2.imshow("Masked and counter-detected Results", imgResult)
    cv2.imshow("Paint on the original image", img)  
    
    
   
   
    
    print(h_min, h_max, sat_min, sat_max, val_min, val_max)
    
    if cv2.waitKey(1) and 0xFF == ord("q"):
        break

    


