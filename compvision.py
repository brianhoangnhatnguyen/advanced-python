import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
loadimage = "img.png"
image = cv2.imread(loadimage)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
access = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
for (x, y, w, z) in access:
    cv2.rectangle(image, (x, y), (x+w, y+z), (0, 255, 0), 2)
cv2.imshow("face_detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
