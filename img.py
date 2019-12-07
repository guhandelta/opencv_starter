import cv2
import numpy

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

# read image
src = cv2.imread("python.jpg", cv2.IMREAD_UNCHANGED)
 
# apply guassian blur on the image
dst = cv2.GaussianBlur(src,(5,5),cv2.BORDER_DEFAULT)
# standard deviation in the X and Y directions, sigmaX and sigmaY respectively. 
# If only sigmaX is specified, sigmaY is taken as equal to sigmaX. 
# If both are given as zeros, they are calculated from the kernel size.
 
# display input and output image
cv2.imshow("Gaussian Smoothing",numpy.hstack((src, dst))) # hstack -> stacks arrays in sequential order to display both images
# the image rgb values are in array, so hstack is used here to display multiple images


cv2.waitKey(5000) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image