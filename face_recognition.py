from pyexpat import features
import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier("haar_face.xml")

people = ["Ben Affleck", "Elton John", "Jerry Seinfeld", "Madonna", "Mindy Kaling"]
# features = np.load("features.npy")
# labels = np.load("labels.npy")

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read("face_trained.yml")

# Enter path of an image in Faces/val
img = cv.imread(r"")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y : y + h, x : x + w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f"Label = {people[label]} with a confidence of {confidence}")

    cv.putText(
        img,
        str(people[label]),
        (10, 30),
        cv.FONT_HERSHEY_COMPLEX,
        0.9,
        (0, 255, 0),
        thickness=1,
    )
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow("Detected face", img)

cv.waitKey(0)
