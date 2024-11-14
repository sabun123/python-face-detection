import cv2
from app.draw_face_boxes import draw_face_boxes

# Simple face detection app
# Takes in a photo and identifies faces

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Three scenarios to test:
# 1. Real faces 
# 2. AI generated faces
# 3. Cartoon faces

group_photo_real = cv2.imread('data/group_photo_real.jpg')
group_photo_ai = cv2.imread('data/group_photo_ai.png')
group_photo_cartoon = cv2.imread('data/group_photo_cartoon.webp')

# images need to be in B/W for the face classifier to work well
gray_photo_real = cv2.cvtColor(group_photo_real, cv2.COLOR_BGR2GRAY)
gray_photo_ai = cv2.cvtColor(group_photo_ai, cv2.COLOR_BGR2GRAY)
gray_photo_cartoon = cv2.cvtColor(group_photo_cartoon, cv2.COLOR_BGR2GRAY)

faces_real = face_classifier.detectMultiScale(gray_photo_real, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
faces_ai = face_classifier.detectMultiScale(gray_photo_ai, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
faces_cartoon = face_classifier.detectMultiScale(gray_photo_cartoon, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))

draw_face_boxes(faces_real, group_photo_real)
draw_face_boxes(faces_ai, gray_photo_ai)
draw_face_boxes(faces_cartoon, gray_photo_cartoon)

cv2.imshow("Real group photo", group_photo_real)
cv2.imshow("AI group photo", group_photo_ai)
cv2.imshow("Cartoon group photo", group_photo_cartoon)

cv2.waitKey(0)
cv2.destroyAllWindows()