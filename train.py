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


# import cv2

# image = cv2.imread('squid.jpg',0)
# mainimage = cv2.imread('squid.jpg')
# cuteimage = cv2.imread('squid.jpg')

# cascad = cv2.CascadeClassifier(r"C:\Users\DobreLi\Desktop\circle\TestCascade\test1\cascade.xml")
# detect = cascad.detectMultiScale(image)
# count = 1

# for (x,y,w,h) in detect:
#     cv2.rectangle(mainimage,(x,y),(x+w,y+h),(0,0,255),2)
#     cv2.putText(mainimage,str(count),(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,255,255),2)
#     # print(str(count),":",x,y,w,h)
#     count +=1

# cv2.imshow("image", mainimage)
# cv2.waitKey(0) 
# cv2.destroyAllWindows() 
# positive = []
# negative = []

# while True:
#     print("Pozitif değer yoksa veya kalmadıysa 0 gir.")
#     sec = input("Pozitif değerleri gir:")
#     if sec == "0":
#         break
#     else:
#         positive.append(str(int(sec)-1))
#         continue
# for pos in positive:
#     p = (detect[int(pos)])
#     for det in detect:
#         if list(p) == list(det):
#             x,y,w,h = det
#             p_read =open(r"C:\Users\DobreLi\Desktop\circle\p.txt","r")
#             all = p_read.readlines()
#             all.append("\n"+rf"C:\Users\DobreLi\Desktop\circle\Img\positive\p(1).jpg 1 {x} {y} {w} {h}")
#             p_write = open(r"C:\Users\DobreLi\Desktop\circle\p.txt","w")
#             for i in all:
#                 print(i)
#                 p_write.write(i)
#             p_read.close()
#             p_write.close()
#         else:
#             x,y,w,h = det
#             n_read =open(r"C:\Users\DobreLi\Desktop\circle\negative.txt","r")
#             all = n_read.readlines()
#             st = all[-1].find('(')
#             en = all[-1].find(')')
#             last =all[-1][st+1:en]
#             n=int(last)+1
#             all.append("\n"+rf"C:\Users\DobreLi\Desktop\circle\Img\negative\n({str(n)}).jpg")
#             n_write = open(r"C:\Users\DobreLi\Desktop\circle\negative.txt","w")
#             for i in all:
#                 n_write.write(i)
#             n_read.close()
#             n_write.close()
#             cute = cuteimage[y:y+h,x:x+w]
#             cv2.imwrite(rf'C:\Users\DobreLi\Desktop\circle\Img\negative\n({str(n)}).jpg',cute) 

# print("*"*100)
# print("Oluşturulacak toplam pozitif değer")
# while True:
#   count_pos = input("Toplam pozitif değer :")
#   if count_pos:
#     break
# p_read =open(r"C:\Users\DobreLi\Desktop\circle\p.txt","r")
# all = p_read.readlines()
# step = (int(count_pos)+50)/len(all)
# c_pos = []
# print(str(step))
# chck = 0
# for i in range(int(step)):
#     print(i)
#     if i>0:
#         a=1
#         for s in all:
#             if a == 1:
#                 c_pos.append("\n"+s)
#                 a = 0
#             else:
#                 c_pos.append(s)
#     else:
#         for s in all:
#             c_pos.append(s)
# print(len(c_pos))
# pos_write =open(r"C:\Users\DobreLi\Desktop\circle\positive.txt","w")
# for c_ in c_pos:
#     pos_write.write(c_)
# p_read.close()
# pos_write.close()

