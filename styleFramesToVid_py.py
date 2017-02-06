import cv2

running = True

out = cv2.VideoWriter('StyledVidPorn.avi',-1, 20.0, (533,400))
i=0
while(i<=139):
#    print ("i : ",i)
    frame = cv2.imread("./video/style_frame{}.jpg".format(i))
    #frame = frame[:,:,::-1]
    i += 1
    out.write(frame)

out.release()
print (" Styled Video Saved ")