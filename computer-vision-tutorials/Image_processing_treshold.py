import cv2  
import numpy as np  

# Read the image
image = cv2.imread("images/tesla.jpg")

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Applying different thresholding techniques on the input grayscale image
#  All pixel values above 100 will be set to 255
ret, thresh_1 = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY)
ret, thresh_2 = cv2.threshold(gray_image, 100, 255, cv2.THRESH_BINARY_INV)
ret, thresh_3 = cv2.threshold(gray_image, 100, 255, cv2.THRESH_TRUNC)
ret, thresh_4 = cv2.threshold(gray_image, 100, 255, cv2.THRESH_TOZERO)
ret, thresh_5 = cv2.threshold(gray_image, 100, 255, cv2.THRESH_TOZERO_INV)
# Applying different adaptive thresholding techniques on the input grayscale image
adap_thresh1 = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                                     cv2.THRESH_BINARY, 199, 5)
adap_thresh2 = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                     cv2.THRESH_BINARY, 199, 5)

#Display the results
cv2.imshow("THRESH_BINARY", thresh_1)
cv2.imshow("THRESH_BINARY_INV", thresh_2)
cv2.imshow("THRESH_TRUNC", thresh_3)
cv2.imshow("THRESH_TOZERO", thresh_4)
cv2.imshow("THRESH_TOZERO_INV", thresh_5)
cv2.imshow("ADAPTIVE_THRESH_MEAN", adap_thresh1)
cv2.imshow("ADAPTIVE_THRESH_GAUSSIAN", adap_thresh2)

ret, otsu_thresh1 = cv2.threshold(gray_image, 120, 255, cv2.THRESH_BINARY + 
                                            cv2.THRESH_OTSU)      
cv2.imshow("Otsu_thresh", otsu_thresh1)
# Wait for a key press and close the windows
if cv2.waitKey(0) & 0xFF == 27:  # 27 is the Esc key
    cv2.destroyAllWindows()
