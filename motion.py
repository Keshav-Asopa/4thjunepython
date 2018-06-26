#python program that will detect the motion of an object using opencv2
import cv2

#function to get the difference of all the three images
def img_diff(x,y,z):
	img1 = cv2.absdiff(x,y)
	img2 = cv2.absdiff(y,z)
	com_d = cv2.bitwise_and(img1,img2)
	return com_d

#turn on the camera
cap = cv2.VideoCapture(0)

#reading only the frame part of read()
frame1 = cap.read()[1]
frame2 = cap.read()[1]
frame3 = cap.read()[1]

#converting the image into grey colour
grey1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
grey2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
grey3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)

while cap.isOpened():
	output = img_diff(grey1,grey2,grey3)
	cv2.imshow("motion",output)
	status, frame = cap.read()

	#will give the new snaps again and again
	grey1 = grey2
	grey2 = grey3
	grey3 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
		
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
