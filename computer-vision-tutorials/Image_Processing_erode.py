import cv2
import numpy as np

kernel = np.zeros((5, 5), np.uint8)

image = cv2.imread("images/tesla.jpg")

# Default erosion
eroded = cv2.erode(src=image, kernel=kernel)

# Iterated Erosion
iterateed_eroded = cv2.erode(src=image, kernel=kernel, iterations=25)

cv2.imshow(winname="Eroded", mat=eroded)
cv2.waitKey(0)