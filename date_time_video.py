import cv2
import datetime

cap = cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    if not ret:
        break
    font = cv2.FONT_HERSHEY_SIMPLEX
    text = 'width:'+ str(cap.get(3))+'Height:'+str(cap.get(4))
    datet = str(datetime.datetime.now())
    frame = cv2.putText(frame,text,(50,50),font, 1,(0,0,0),2,cv2.LINE_AA)
    frame = cv2.putText(frame,datet,(100,100),font, 1,(0,0,0),2,cv2.LINE_AA)
    cv2.imshow('image',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()