import cv2
import numpy as np

filter = np.ones((5, 5), np.uint8) # kernel (filter)

img = cv2.imread(".venv/resources/image.jpeg")

imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Dispay in grayscale
imBlur = cv2.GaussianBlur(imGray, (7, 7), 0) # Display in Blur ; (image, filter, sigmaX)
imgCanny = cv2.Canny(img, 100, 100) # Display with the Edge Detector, in particular one called "Canny"; (image, treshold 1, treshold 2)
imgCannyLow = cv2.Canny(img, 200, 200) # Increasing threshold allows to REDUCE the density of edges 
imgDialation = cv2.dilate(imgCanny,kernel=filter, iterations=1 ) # Increase the thickness of edges.As the iteration increases, edges get  thicker
imgEroded = cv2.erode(imgDialation, kernel=filter, iterations=1) # Decreasing the thickness of edges.As the iteration increases, edges get thinner


cv2.imshow("Gray image", imGray)
# cv2.waitKey(0)  # pasing 0 allows to not to close until clicked exit

cv2.imshow("Blurry image", imBlur)

cv2.imshow("Canny Edge Detector image", imgCannyLow)

cv2.imshow(" Thickened edges (Dialation) image", imgDialation)

cv2.imshow(" Thinned edges (Eroded) image", imgEroded)

cv2.waitKey(0)  # pasing 0 allows to not to close until clicked exit

###############################################################






