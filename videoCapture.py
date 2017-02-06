import cv2

num_secs = 5
fps = 20.0

webcam = cv2.VideoCapture(0)

webcamReso = (int(webcam.get(cv2.CAP_PROP_FRAME_WIDTH)),int(webcam.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# Above line for opencv version 3...below line for opencv version 2.x
#webcamReso = (int(webcam.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),int(webcam.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

print (webcamReso)
# fourcc = cv2.VideoWriter_fourcc(*"XVID")
# Above line for opencv version 3...below line for opencv version 2.x
# fourcc = cv2.cv.CV_FOURCC(*"DIVX") #or XVID

# out = cv2.VideoWriter('VidPron.avi',fourcc, 20.0, (webcam.get(cv2.CV_CAP_PROP_FRAME_WIDTH),webcam.get(cv2.CV_CAP_PROP_FRAME_WIDTH)))
# Above line for opencv version 3...below line for opencv version 2.x

out = cv2.VideoWriter('VidPorn.avi',-1, fps, webcamReso)

no_frames = num_secs*fps
ctr = 0

while(webcam.isOpened()):

    ret, frame = webcam.read()
    ctr += 1
    frame = cv2.flip(frame,1)
    out.write(frame)
    cv2.imshow('VidPorn',frame)

    if cv2.waitKey(1) == 27 or (ctr>no_frames):   #ESC
        break

webcam.release()
out.release()
cv2.destroyAllWindows()

print (" Video Saved ")
