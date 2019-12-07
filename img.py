import cv2

img = cv2.imread("ac4.jpg",0) # 1 - read img in color || 0 - read img n b/w || -1 - read img in color, with transparency
print(img)
print(type(img))
cv2.imshow("show",img)
cv2.waitKey(5000)
cv2.destroyAllWindows()