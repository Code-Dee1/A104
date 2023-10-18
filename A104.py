import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img, "The Sun",(20,50), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img, "Mercury",(98,190), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img, "Venus",(190,290), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img, "Earth",(280,150), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img, "Mars",(375,290), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img, "Jupiter",(550,40), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img, "Saturn",(750,320), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img, "Uranus",(950,130), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1,color=(0,0,255))
cv2.putText(img, "Neptune",(1090,300), fontFace=cv2.FONT_HERSHEY_SCRIPT_COMPLEX,fontScale=1,color=(0,0,255))


cv2.imshow("systems", img)
cv2.waitKey(0)