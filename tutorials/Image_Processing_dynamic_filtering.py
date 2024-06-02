import cv2
import numpy as np

def empty():
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Saturation Min", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Saturation Max", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Value Min", "TrackBars", 40,255,empty)
cv2.createTrackbar("Value Max", "TrackBars", 255,255,empty)




cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
while(1):
    _, frame = cap.read()
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars" )
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars" )
    
    sat_min = cv2.getTrackbarPos("Saturation Min", "TrackBars")
    sat_max = cv2.getTrackbarPos("Saturation Max", "TrackBars")
    
    val_min = cv2.getTrackbarPos("Value Min", "TrackBars")
    val_max = cv2.getTrackbarPos("Value Max", "TrackBars")
    
    lower_bound = np.array([h_min, sat_min, val_min])
    upper_bound = np.array([h_max, sat_max, val_max])
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lowerb=lower_bound, upperb=upper_bound)
    
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    
    cv2.imshow("Result", result)
    
    if cv2.waitKey(1) & 0XFF == ord("q"):
        break
cv2.destroyAllWindows()
cap.release()