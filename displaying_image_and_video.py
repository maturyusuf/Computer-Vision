import cv2
print("Package imported")

##########################################
### Displaying image & Video Captures ####
##########################################


# Displaying image
img = cv2.imread(".venv/resources/image.jpeg")
cv2.imshow("Output", img)
cv2.waitKey(1000) # Delay by miliseconds


# Displaying Video
cap = cv2.VideoCapture(".venv/resources/video.mp4")

# It shows every frame in the video
while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(10) & 0xFF == ord("q"): # Loop breaks if pressed "q" key
        break