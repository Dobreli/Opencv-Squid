import cv2


image = cv2.imread('squid.jpg',0)
mainimage = cv2.imread('squid.jpg')

triangle = cv2.CascadeClassifier(r"cascade\triangle.xml")
circle = cv2.CascadeClassifier(r"cascade\circle.xml")
star = cv2.CascadeClassifier(r"cascade\star.xml")
umbrella = cv2.CascadeClassifier(r"cascade\umbrella.xml")

cv2.imshow("image", mainimage)

cascadelist = [umbrella,circle,triangle,star]
namelist = ["umbrella","circle","triangle","star"]
count = 0
for i in cascadelist:
    cv2.waitKey(3000) 
    detect = i.detectMultiScale(image)
    for (x,y,w,h) in detect:
        cv2.rectangle(mainimage,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.putText(mainimage,str(namelist[count]),(x-10,y+100),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,0),2)
        cv2.imshow("image", mainimage)
        count +=1

cv2.waitKey(0)
cv2.destroyAllWindows() 
