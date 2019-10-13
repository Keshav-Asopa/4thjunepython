## Importing library
import cv2

#calling CascadeClassifier 
#data.xml file contain data such as face dimensions of humane face
face_data = cv2.CascadeClassifier('data.xml')
#camera is switch on
cap = cv2.VideoCapture(0)

# Collecting frames with loop
while cap.isOpened():
	status, img = cap.read()
	
	# converting frame to grey scale
	grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	#detecting face as per the data store	
	faces = face_data.detectMultiScale(grayimg,1.15,5)	
	
	# Making a box around face
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
		roi_gray = grayimg[y:y+h,x:x+w]
		roi_color = img[y:y+h , x:x+w]
	# Show the edited image
	cv2.imshow('img1',img)
	#exit the program	
	if cv2.waitKey(30) & 0xFF == ord('q'):
		break

# relaesing the camera module
cap.release()
cv2.destroyAllWindows()
	
		
