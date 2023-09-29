import cv2
import numpy as np

####################################################################
# FEATURE CHANGING WITH TRACKBARS
####################################################################
# Turning the color into HSV nad check it with Trackbars ** 
def empty():
    pass



PATH = ".venv/resources/image.jpeg"
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0,179,empty)


img = cv2.imread(PATH)
imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image", imgHSV) # Turning the color into HSV


# Now let's use trackbar to change some features 
tbWindow = "Changing Features with TrackBars"
cv2.namedWindow(tbWindow)
cv2.resizeWindow(tbWindow, 640, 240)
cv2.createTrackbar("Hue Min", tbWindow, 123,179,empty)
cv2.createTrackbar("Hue Max", tbWindow, 155,179,empty)
cv2.createTrackbar("Saturation Min", tbWindow, 53,255,empty)
cv2.createTrackbar("Saturation Max", tbWindow, 255,255,empty)
cv2.createTrackbar("Value Min", tbWindow, 40,255,empty)
cv2.createTrackbar("Value Max", tbWindow, 255,255,empty)

while True:
    img = cv2.imread(PATH)
    h_min = cv2.getTrackbarPos("Hue Min", tbWindow)
    h_max = cv2.getTrackbarPos("Hue Max", tbWindow)
    sat_min = cv2.getTrackbarPos("Saturation Min", tbWindow)
    sat_max = cv2.getTrackbarPos("Saturation Max", tbWindow)
    val_min = cv2.getTrackbarPos("Value Min", tbWindow)
    val_max = cv2.getTrackbarPos("Value Max", tbWindow)
    print(h_min,h_max,sat_min,sat_max,val_min,val_max)
    
    lower = np.array([h_min,  sat_min, val_min, ])
    upper = np.array([h_max, sat_max, val_max])
    mask = cv2.inRange(imgHSV, lowerb=lower, upperb=upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask) # bitwise; creates 3rd image out of given to.If a pixel is present in both, it takes it as yes and stores in the new image
    
    cv2.imshow("Original", img)
    cv2.imshow("HSV Image", imgHSV) # Turning the color into HSV
    cv2.imshow("Mask", mask)
    cv2.imshow("imgResult", imgResult)
    cv2.waitKey(1)