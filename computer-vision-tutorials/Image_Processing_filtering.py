import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    # Converting from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_beige = np.array([34,0,0 ])
    upper_beige = np.array([100,255,255 ])
    
    mask = cv2.inRange(hsv, lowerb=lower_beige, upperb=upper_beige)
    result = cv2.bitwise_and(frame, frame, mask = mask)
    
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()

