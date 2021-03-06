import cv2
from mtcnn.mtcnn import MTCNN

detector=MTCNN()
vid=cv2.imread("resources/img_1.png")
faces=detector.detect_faces(vid)
print(faces)