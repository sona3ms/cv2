import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')#'X','v','I','D'
out = cv2.VideoWriter('output.avi',fourcc, 20.0,(640,480))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
while(True):#capture the frames
    ret, frame=cap.read()#ret will return true/false if we capture the frame, 'frame' save the frame
    # if not ret:
    #     print("Error: Could not read a frame.")
    #     break
    cap.set(3,6400)
    cap.set(4,4800)
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # out.write(frame)
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)#gray akkan
   
    cv2.imshow('live_image',frame)
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#release the capture variable
cap.release()
out.release()
cv2.destroyAllWindows()