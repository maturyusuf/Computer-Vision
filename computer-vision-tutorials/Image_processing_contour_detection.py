import cv2
import numpy as np

image = cv2.imread("images/shapes.jpg")

imGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

imBlur = cv2.GaussianBlur(imGray, (5, 5), 2)

# cv2.imshow("Original", image)
# cv2.imshow("Gray İmage", imGray)
# cv2.imshow("Blurred Image", imBlur)



imgCanny = cv2.Canny(imBlur, 50, 50)

imContor = imBlur.copy()
cv2.imshow("Canny Edge Detection",imgCanny)

def getContor(image):
    contours, hiearchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(f"Area:{area} " )
        if(area > 10 ):
            cv2.drawContours(imContor, cnt, contourIdx=-1, color=(255,0,0), thickness=2)
            peri = cv2.arcLength(cnt, True)
            print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx)) # givers the corner
            objCor= len(approx)
            x,y,w,h = cv2.boundingRect(approx)
            if objCor == 4.0:
                objectType = "Rectangle"
                
            cv2.rectangle(imContor, (x,y), (x + w, y + h) , (255,0,0),thickness=3 )
            cv2.putText(imContor, text="Rectangele", color=(255,0,0), thickness=2,
                        org=(x + (w//2) - 10, y + (h //2) - 10),
                         fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5,)

getContor(imgCanny)
cv2.imshow("Countured/shape detected Image", imContor)
cv2.waitKey(0)