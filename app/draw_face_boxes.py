import cv2

def draw_face_boxes(cv2_faces, photo):
  for (x, y, w, h) in cv2_faces:
    cv2.rectangle(photo, (x, y), (x + w, y + h), (255, 0, 0), 2)