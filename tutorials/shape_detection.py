import cv2
import numpy as np

PATH = ".venv/resources/shapes.jpg"
img = cv2.imread(PATH)

imContor = img.copy()

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)

cv2.imshow("Original", img)
cv2.imshow("Gray", imgGray)
cv2.imshow("Blured Gray", imgBlur)

imgCanny = cv2.Canny(imgBlur, 50, 50)

# imgBlank = np.zeros_like(img)


cv2.imshow("Edge Detection with Canny",imgCanny)

def getContors(img):
    contours, heirarchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE ) # RETR_EXTERNAL is really good mode for finding outer corners in regards to the contours
    for cnt in contours:
       area = cv2.contourArea(cnt)
       print( area) 
       if area > 500:
        cv2.drawContours(imContor, cnt, contourIdx=-1, color=(255, 0, 0),thickness=3)
        peri = cv2.arcLength(cnt, True) # LENGTH OF CONTOUR
        print(peri)
        approx = cv2.approxPolyDP(cnt, 0.02*peri, True) # APPROXIMATE THE POLY TO GET CORNER POINTS,(image, resolution(epsilon), closed)
        print(len(approx)) # gives the corner
        objCor = len(approx)
        x,y,w,h = cv2.boundingRect(approx)
        objectType = "None"
        if objCor  == 4.0:
            objectType = "Rectangle"
            
        cv2.rectangle(imContor, (x,y), (x + w, y + h), (0,255,0), 2)
        cv2.putText(imContor, text=objectType, color=(0,255,0), thickness=2, 
                    org=(x +(w//2) - 10, y + (h//2) - 10),
                    fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.5,)
getContors(imgCanny)
cv2.imshow("Contoured/Shape Detected",imContor)
cv2.waitKey(0)