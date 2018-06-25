#this is python3 program used to copy some portion of a image and to add on another image

#importing the libraries
import cv2

#loading the image from which a part of image is to be copied
img = cv2.imread("dog.jpg")

#loading the image on which part of another image is to be pasted
img1 = cv2.imread("dog1.jpeg")

#saving and copying the part of image into another image roi(region of interest)
roi = img[200:350 , 100 :250]         #coordinates of the rectangle form are (100,200) and (250,350)

#printing the shape of copied part i.e, roi
print(roi.shape)

#cheching the shape of an image onto which copied part is to be pasted
print(img1.shape)

#printing the number of rows of the copied part
print(roi.shape[0])

#printing the number of coloumns of the copied part
print(roi.shape[1])

#pasting the copied part onto another image with starting co-ordinate (10,20) 
img1[10:roi.shape[0]+10 , 20:roi.shape[1]+20]=roi

#printing the image from which a part is copied
cv2.imshow('img', img)

#printing the copied part
cv2.imshow('roi', roi)

#printing the image on which a part is pasted
cv2.imshow('img1', img1)

#holding the screen to display the image for infinite time
cv2.waitKey(0)



