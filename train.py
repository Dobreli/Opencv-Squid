import cv2

image = cv2.imread('squid.jpg',0)
mainimage = cv2.imread('squid.jpg')
cuteimage = cv2.imread('squid.jpg')

cascad = cv2.CascadeClassifier("cascade.xml")
detect = cascad.detectMultiScale(image)
print(detect)
count = 1

for (x,y,w,h) in detect:
    cv2.rectangle(mainimage,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.putText(mainimage,str(count),(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,255),2)
    cute = cuteimage[y:y+h,x:x+w]
    cv2.imwrite(rf'C:\Users\Desktop\circle\Out\{count}.jpg',cute) 
    count +=1

    

cv2.imshow("image", mainimage)
cv2.waitKey(0) 
cv2.destroyAllWindows() 
