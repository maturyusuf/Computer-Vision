# Check for installation
import cv2 
import numpy as np

print(cv2.__version__)

# Reading the image
image = cv2.imread("tesla.jpg")

print(image)
print(type(image))
print(image.shape)
# Height and Width
h, w = image.shape[:2]
print(f"Height:={h}, Width={w}")

# Extracting Color Values
pixel = image[100, 100]
(R, G, B) = pixel
print("Red:{}, Green: {}, Blue: {}".format(R, G, B))

# Displaying the image
cv2.imshow("image",image)
cv2.waitKey(delay=3000)

# Closing all open windows 
cv2.destroyAllWindows() 