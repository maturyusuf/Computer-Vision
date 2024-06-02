import cv2
import numpy as np
# Check setosa.io: https://setosa.io/ev/image-kernels/

# Face Cascade
faceCascadePath = cv2.data.haarcascades + "haarcascade_frontalface_alt.xml"
faceCascadeClasifier = cv2.CascadeClassifier(faceCascadePath)
img = cv2.imread("C:/Users/user/computer-vision-tutorials/faces.jpg")
imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascadeClasifier.detectMultiScale(imGray, 1.1, 1)

for (x,y,w,h) in faces:
    cv2.putText(img=img, 
                text="Face", 
                org=(x+5, y-5), 
                color=(122,210,50), 
                fontScale=0.5, 
                thickness=1, 
                fontFace=cv2.FONT_HERSHEY_COMPLEX)
    cv2.rectangle(color=(122,210,50), img=img, pt1=(x,y), pt2=(x+w, y+h), thickness=2)
    
    cv2.imshow("Image", img)
    
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
    
    