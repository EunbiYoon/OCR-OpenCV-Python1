import cv2
import pytesseract
import datetime
import pandas as pd

pytesseract.pytesseract.tesseract_cmd="C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
img=cv2.imread('plate.png')

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_boxes(img)) # 글자의 위치를  알수 있음

## Detecting Characters with [character, x,y,w,h] 네모 박스쳐서 글자 인식함
hImg,wImg,_ =img.shape
boxes=pytesseract.image_to_boxes(img)

c=''

for b in boxes.splitlines():
    #print(b)
    b= b.split(' ')
    print(b) #[character, x,y,w,h]
    c = b[0] + c
    x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
    cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
    cv2.putText(img,b[0],(x,hImg-y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
c = c[::-1]

now = datetime.datetime.now()
now = now.strftime("%Y/%m/%d %H:%M:%S")

#today=today.strftime('%m/%d')
d=pd.DataFrame()
d.at[1,"Car Plate No"]=c
d.at[1,"Time"]=now
d.to_excel('2.xlsx')
print(d)


# ## Detecting Words word 자체로 인식한다
# hImg,wImg,_ =img.shape
# boxes=pytesseract.image_to_data(img)
#
# for x,b in enumerate(boxes.splitlines()):
#     #print(b)
#     if x!=0:
#         b= b.split()
#         print(b)
#         if len(b)==12:
#             x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9]) # 6,7,8,9 번째 원소가 bounding box 나타냄
#             cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),3)
#             cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)




# ## Character 단위로 숫자만 인식한다.
# ## Detecting Characters with [character, x,y,w,h] 네모 박스쳐서 글자 인식함
# hImg,wImg,_ =img.shape
# cong=r'--oem 3 --psm 6 outputbase digits'
# boxes=pytesseract.image_to_boxes(img,config=cong)
#
# for b in boxes.splitlines():
#     #print(b)
#     b= b.split(' ')
#     print(b) #[character, x,y,w,h]
#     x,y,w,h=int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),3)
#     cv2.putText(img,b[0],(x,hImg-y+25),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)





# ## 단어단위로 숫자만 인식한다.
# hImg,wImg,_ =img.shape
# cong=r'--oem 3 --psm 6 outputbase digits'
# boxes=pytesseract.image_to_data(img,config=cong)
#
# for x,b in enumerate(boxes.splitlines()):
#     #print(b)
#     if x!=0:
#         b= b.split()
#         print(b)
#         if len(b)==12:
#             x,y,w,h=int(b[6]),int(b[7]),int(b[8]),int(b[9]) # 6,7,8,9 번째 원소가 bounding box 나타냄
#             cv2.rectangle(img,(x,y),(w+x,h+y),(0,0,255),3)
#             cv2.putText(img,b[11],(x,y),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
#
#


cv2.imshow('result',img)
cv2.waitKey(0)
