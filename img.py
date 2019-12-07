import cv2

img = cv2.imread("ac4.jpg",0) # 1 - read img in color || 0 - read img n b/w || -1 - read img in color, with transparency
rs = cv2.resize(img,(int(img.shape[0]/2),int(img.shape[1]/2))) # img.shap[0] => height || img.shape[1] => width
rs1 = cv2.resize(img,(int(img.shape[0]/0.5),int(img.shape[1]/3)))
print(img)
print(type(img))
edges = cv2.Canny(img,100,200)
cv2.imwrite("resize.jpg",rs)
cv2.imwrite("resize1.jpg",rs1)
cv2.imshow("show",img)
cv2.imshow("Edges Detected",edges)

cv2.waitKey(5000) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image