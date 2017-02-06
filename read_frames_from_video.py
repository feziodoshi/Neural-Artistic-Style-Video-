import cv2
import NetworkFunction as s

webcamReso = (533,400)
out = cv2.VideoWriter('StylizedVidPorn.avi',-1, 20.0, webcamReso)


def read_frames_from_video():
	cap = cv2.VideoCapture('VidPorn.avi')
	frame_count = 0
	start_fram = 123
	choose_iter=[1,2,3,4,4,3,2]
	while cap.isOpened():
		iter = choose_iter[int(frame_count/20)]
		ret, frame = cap.read()
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

		if(frame_count>start_fram):
			style_frame = s.Stylize(frame,"./images/inputs/style/seated-nude.jpg","./output/first_try_bro", arg_num_iter = iter)
			#make_video(style_frame)
			out.write(style_frame)
			cv2.imwrite('./video/style_frame%d.jpg'%frame_count, style_frame)
		else:
			style_frame = frame


		frame_count += 1
		if ret == True:
			cv2.imshow("video", style_frame)
			if (cv2.waitKey(1) & 0xFF == ord('q')):
				break
		else:
			break

	cap.release()
	out.release()
	cv2.destroyAllWindows()


read_frames_from_video()

