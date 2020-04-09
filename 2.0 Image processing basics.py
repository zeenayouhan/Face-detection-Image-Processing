import cv2

img=cv2.imread('samples/flower.jpg')


cv2.rectangle(img,(40,40),(140,140),(0,255,0),2)
cv2.putText(img,'RECTANGLE1',(40,40),cv2.FONT_HERSHEY_SIMPLEX,1,(233,255,25),2)

cv2.imshow('FLOWER',img)
