import cv2

img = cv2.imread(".venv/resources/faces.png")

# Face Cascade
faceCascadePath = cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml'
faceCascadeClassifier = cv2.CascadeClassifier(faceCascadePath)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascadeClassifier.detectMultiScale(imgGray, 1.1, 1)

for (x,y,w,h) in faces:
    cv2.putText(img=img, text="Face",org=(x+5,y-5), color=(122,210,50), fontScale=0.5, thickness=1, fontFace=cv2.FONT_HERSHEY_COMPLEX)
    cv2.rectangle(img, (x,y), (x+w, y+w), (255,0,0), 2)


cv2.imshow("Faces Image",  img)


###################################################


winName = "Face Detection Through Camera"
cap = cv2.VideoCapture(0)
cap.set(3, 500)
cap.set(4, 500)
cap.set(10, 100)

while True:
    succes, img = cap.read()
    
    
    faceCascadePath = cv2.data.haarcascades + "haarcascade_frontalface_alt.xml"
    imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faceCascadeClassifier = cv2.CascadeClassifier(faceCascadePath)
    faces = faceCascadeClassifier.detectMultiScale(imGray, (1.1), 4)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, "The Sexiest Guy Alive", (x + 10, y - 10),color=(0, 255, 0), fontFace= cv2.FONT_HERSHEY_SIMPLEX, thickness=2,fontScale=0.5 )
    cv2.imshow(winName, img)
    if cv2.waitKey(1) and 0x0F == ord("q"):
        break