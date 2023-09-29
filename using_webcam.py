import cv2

########################
### Using Webcam #######
########################

cap = cv2.VideoCapture(0)
cap.set(3, 640) # width: 640 (id number of the width is 3)
cap.set(4, 480) # height: 640 (id number of the height is 4)
cap.set(10, 100) # Adjusting the Brightness

while True:
    success, img = cap.read()
    cv2.imshow("Output",img)
    if cv2.waitKey(1) &  0xFF == ord("q"): # breaks the lop if pressed "q   "
        break