import cv2

img_1 = cv2.imread("images/add_1.jpg") 
img_2 = cv2.imread("images/add_2.jpg") 

### ADDITION ###

weightedSum = cv2.addWeighted(img_1, 
                              0.5,
                              img_2,
                              0.4,
                              0)
# Displaying weighted image
cv2.imshow("Weighted Image",weightedSum)


# De-allocating any associated memory space and allows to use 'ESC' lose the window.
if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()  

### SUBTRACTION ###
img_1 = cv2.imread("images/sub_1")
img_2=  cv2.imread("images/sub_2")


