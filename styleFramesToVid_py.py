import cv2

# video writer for writing the frames into the video
out = cv2.VideoWriter('StyledVidPorn.avi',-1, 20.0, (533,400))
i=0
while(i<=139):
    # print ("i : ",i)
    # read each style frame present in the folder 
    frame = cv2.imread("./video/style_frame{}.jpg".format(i))
    # frame = frame[:,:,::-1]
    i += 1
    # write frame in video
    out.write(frame)

out.release()
print (" Styled Video Saved ")
