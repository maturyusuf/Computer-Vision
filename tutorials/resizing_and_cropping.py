import cv2

# in cv2 coordinat system is:
# ------------------- x
# |(0, 0)
# |
# |
# |
# |
# |
# y

img = cv2.imread(".venv/resources/image.jpeg")

imgResized = cv2.resize(img, (300, 200))
print(imgResized.shape)

cv2.imshow("Image", img)
cv2.imshow("Resized image", imgResized)

# Cropping

imgCropped = img[0:200, 200:500]
cv2.imshow("Crooped image", imgCropped)


cv2.waitKey(0)