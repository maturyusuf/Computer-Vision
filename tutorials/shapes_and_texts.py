###########################
### Drawing some stuff #####

import cv2
import numpy as np

img = np.zeros((512, 512,3))  # All black
print("Shape of the image: ", img.shape)

#img[:] = 255,0,0 # All blue
print(img[:])

#img[200:300, 150:250] = 255,0,0 # All blue
# cv2.imshow("Image", img)




# Creating Line

cv2.line(img, (0, 0), (300, 300), (0,250,250))
cv2.imshow("Image", img)


cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0,250,250)) # A diagonal line all the way
cv2.imshow("Image", img)


# Creating Rectangle
cv2.rectangle (img, (0, 0), (250, 350),color=(0, 125, 100))
cv2.imshow("Image", img)


# Creating filled Rectangle
cv2.rectangle (img, (0, 0), (250, 350),(0, 125, 100), thickness=cv2.FILLED)
cv2.imshow("Image", img)


# Creating Circle
cv2.circle (img, (400, 60), 30,(0, 125, 100), thickness=5)

cv2.putText(img, "OPEN CV TUTORIAL", org=(150, 300), color=cv2.COLORMAP_MAGMA, fontScale=1, thickness=1, fontFace=cv2.FONT_HERSHEY_COMPLEX)
cv2.imshow("Image", img)
cv2.waitKey(0)
