import cv2

"""
Color spaces: Color spaces are a way to represent the color channels present in the image that gives the image that 
particular hue.

BGR color space: OpenCV’s default color space is RGB. However, it actually stores color in the BGR format. 
It is an additive color model where the different intensities of Blue, Green and Red give different shades of color.

HSV color space: It stores color information in a cylindrical representation of RGB color points. It attempts to 
depict the colors as perceived by the human eye. Hue value varies from 0-179, Saturation value varies from 0-255 
and Value value varies from 0-255. It is mostly used for color segmentation purpose.

CMYK color space: Unlike, RGB it is a subtractive color space. The CMYK model works by partially or entirely 
masking colors on a lighter, usually white, background. The ink reduces the light that would otherwise be reflected.
Such a model is called subtractive because inks “subtract” the colors red, green and blue from white light. 
White light minus red leaves cyan, white light minus green leaves magenta, and white light minus blue leaves yellow.

"""

image = cv2.imread("colorful.jpg")

#Seperating different color channels
B, G ,R = cv2.split(image)

cv2.imshow("Original", image)
cv2.waitKey(0)

cv2.imshow("Blue", B)
cv2.waitKey(0)

cv2.imshow("Green", G)
cv2.waitKey(0)

cv2.imshow("Red", R)
cv2.waitKey(0)

cv2.destroyAllWindows()