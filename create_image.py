import cv2

img = cv2.imread('solar-system.jpg')
cv2.putText(img,'Sol',(70,50),cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,255),2) #texto do sol

cv2.putText(img,'Mercurio',(110,250),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,255),1) #texto de mercúrio

cv2.putText(img,'Venus',(190,170),cv2.FONT_HERSHEY_TRIPLEX,0.5,(255,255,0),1) #texto de vênus

cv2.putText(img,'Terra',(290,270),cv2.FONT_HERSHEY_TRIPLEX,0.5,(255,0,255),1) #texto de terra

cv2.putText(img,'Marte',(380,170),cv2.FONT_HERSHEY_TRIPLEX,0.5,(0,255,0),1) #texto de marte

cv2.putText(img,'Jupiter',(520,400),cv2.FONT_HERSHEY_TRIPLEX,1,(255,150,0),2) #texto de júpiter

cv2.putText(img,'Saturno',(700,320),cv2.FONT_HERSHEY_TRIPLEX,1,(255,0,0),2) #texto de saturno

cv2.putText(img,'Urano',(940,140),cv2.FONT_HERSHEY_TRIPLEX,1,(0,0,255),2) #texto de urano

cv2.putText(img,'Netuno',(1080,140),cv2.FONT_HERSHEY_TRIPLEX,1,(0,150,255),2) #texto de netuno

cv2.imshow('Sistema_Solar',img)
cv2.waitKey(0)
print(img)

