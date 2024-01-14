import cv2

image= cv2.imread("solar-system.jpg")
cv2.putText(image,"Sun",(100,100,),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale= 1, color=(255,255,255))
cv2.putText(image,"Mercury",(110,200),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale= 0.5, color=(255,255,255))
cv2.putText(image,"Venus",(190,250),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale= 0.5, color=(255,255,255))
cv2.putText(image,"Earth",(275,175),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale= 0.5, color=(255,255,255))
cv2.putText(image,"Mars",(380,190),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale= 0.5, color=(255,255,255))
cv2.putText(image,"Jupiter",(550,70),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale= 0.5, color=(255,255,255))
cv2.putText(image,"Saturn",(790,125),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale= 0.5, color=(255,255,255))
cv2.putText(image,"Uranus",(960,130),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale= 0.5, color=(255,255,255))
cv2.putText(image,"Neptune",(1100,140),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale= 0.5, color=(255,255,255))

cv2.imshow("window",image)

cv2.waitKey(0)