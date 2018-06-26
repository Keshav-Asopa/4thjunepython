# A python program to copy the part of image from webcam and put it on another image

import cv2

#loading the image on which part of another image is to be pasted
img1 = cv2.imread("dog1.jpeg")

print("Press 'c' to capture the photo")
print("press 'q' to exit")

#to start the webcam or external web camera
capture = cv2.VideoCapture(0)

#camera will switch on
while capture.isOpened():
		
	status,frame = capture.read()
	#to draw a rectangle on a frame
	cv2.rectangle(frame,(100,100),(250,250),(0,0,255),2)	
	cv2.imshow("frame1",frame)
	
	if cv2.waitKey(1) & 0xFF == ord("c")  :
	#saving and copying the part of image into another image roi(region of interest)
		roi = frame[100:250 , 100 :250]         #coordinates of the rectangle form are (100,100) and (250,250)

		#pasting the roi on another image
		img1[50:roi.shape[0]+50, 50:roi.shape[1]+50] = roi
		cv2.imshow("final_result", img1)
		cv2.imshow("f1", frame)
	
		#saving the image
		cv2.imwrite("final_image.jpeg",img1)	
		capture.release()
		cv2.waitKey(0)
		#exit the program
		if cv2.waitKey(1) & 0xFF == ord("q")  : 
			break

