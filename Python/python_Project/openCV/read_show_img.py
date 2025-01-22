import cv2
import numpy as np
import os

# img=cv2.imread(r"D:\SHAFIUL MONDOL\Python\python_Project\openCV\sh.jpg")
# re=cv2.resize(img,(200,200))
# double=np.hstack((re,re))
# fo=np.vstack((double,double))
# cv2.imshow("shafiul",fo)h
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# # print(img)
list_name=os.listdir(r"C:\Users\MD SHAFIUL ISLAM\OneDrive\Pictures\Screenshots")

for name in list_name:
    path="C:\\Users\\MD SHAFIUL ISLAM\\OneDrive\\Pictures\\Screenshots"
    img_name=path+"\\"+name
    img=cv2.imread(img_name)
    re=cv2.resize(img,(200,200))
    cv2.imshow("immage",img)
    cv2.waitKey(0)
cv2.destroyAllWindows()
