import cv2


### SUBTRACTION ###
img_1 = cv2.imread("images/sub_1.jpg")
img_2=  cv2.imread("images/sub_2.jpg")

# Subtract two images
subtracted=cv2.subtract(img_1, img_2)


cv2.imshow("Subtracted Image",subtracted)

# De-allocating any associated memory space and allows to use 'ESC' lose the window.
if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows() 