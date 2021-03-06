import cv2
import os
facecascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
vid=cv2.VideoCapture("tenet opencv.avi")
fourcc=cv2.VideoWriter_fourcc(*'MPEG')

out=cv2.VideoWriter("v12.avi",fourcc,20,(int(vid.get(3)),int(vid.get(4))))

while True:
    sucess,frames=vid.read()
    if not sucess:
        print("frames not read exiting")

    imgray=cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
    faces=facecascade.detectMultiScale(imgray,1.1,4)
    for(x,y,w,h) in faces:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,200),2)

    out.write(frames)
    cv2.imshow("video",frames)



    if cv2.waitKey(1)& 0xff==ord(" "):
        break



vid.release()
cv2.destroyAllWindows()







