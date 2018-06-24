#importing the libraries
import cv2
import random

#starting the camera
capture = cv2.VideoCapture(0)

#checking the loop
while capture.isOpened() : 
	print("\nThe camera is running and ready to take the pictures ")
	status, frame = capture.read()
	#to create a image as a black and white image of the frame	
	bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#to draw a rectangle on a frame
	cv2.rectangle(frame,(100,100),(200,200),(0,0,255),2)
	#to add a text on a frame
	font = cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(frame,"classroom",(100,100),font,2,(255,0,0),cv2.LINE_AA)
	#to display the image
	cv2.imshow("frame1",frame)
	cv2.imshow("frame2",bw)
	#saving the images using random function
	x= random.random()
	y = str(x)[2:6]
	cv2.imwrite("adhoc"+y+".jpg",frame)
	#to hold the screen and to stop the camera by pressing q i.e, to break off from the while loop 0xFF is used to take the input from gthe keyboard
	if cv2.waitKey(1) & 0xFF == ord("q")  : 
		break
#to destroy or to close all the windows
cv2.destroyAllWindows()
#to close the camera using release function
capture.release()



