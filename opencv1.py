#importing the libraries
import cv2

#loading the image NOTE:- the program file and the image which is to be loaded should be on the same location
img = cv2.imread("dog1.jpeg")

#printing the dog image in black and white form...0 is used 
img1 = cv2.imread("dog.jpg",0)

#printing the image in the numpy format
print(img)

#printing the first pixel of the image
print(img[0][0])

#changing the color of first pixel of the image
img[0][0]= (0, 0, 0)

#printing the shape of the image
print(img.shape)
print(img1.shape)

#performing operations on the image
#drawing a line on the image
cv2.line(img,(0,0),(100,100),(0,255,0),2)

#drawing a rectangle on the image
cv2.rectangle(img1,(320,50),(800,350),(255,0,0),2)

#Drawing a ciecle onto the image
cv2.circle(img1,(570,220),100,(0,0,255),4)

#writing text on the image
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"DOG",(30,70),font,2,(100,23,100),cv2.LINE_AA)

#displaying the image
cv2.imshow("Window",img)
cv2.imshow("bwdog",img1)

#saving the black and white image of the dog as a new file
cv2.imwrite("newdog.jpeg",img1)

#to hold the image
cv2.waitKey(0) 
