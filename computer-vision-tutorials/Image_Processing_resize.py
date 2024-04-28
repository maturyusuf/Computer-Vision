import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("images/colorful.jpg")

# Shrinking image on x and y planes
half = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)
cv2.imshow("Half", half)

# Changing image size by defining new size
new_size = cv2.resize(image, dsize=(500, 500))

cv2.imshow("New Size", new_size)
 
print("Original Size: {}".format(image.shape))
print("New Size: {}".format(new_size.shape))

# Using itnerpolations:
"""
cv2.INTER_AREA: Bir görseli küçültmemiz gerektiğinde kullanılır.
cv2.INTER_CUBIC: Bu yavaş ama daha verimlidir.
cv2.INTER_LINEAR: Bu öncelikle yakınlaştırma gerektiğinde kullanılır. Bu, OpenCV'deki varsayılan enterpolasyon tekniğidir.
"""

interpolated = cv2.resize(image, (600, 600), interpolation=cv2.INTER_CUBIC)
cv2.imshow("Interpolated", interpolated)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()