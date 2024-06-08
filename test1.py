import cv2
# Read an Image File
img=cv2.imread("image/flower.jpg")
# to view the image
cv2.imshow("original image",img)

# Changing Colorspace
img2=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# save the gray image using imwrite function
cv2.imwrite("image/flower_gray.jpg",img2)
cv2.imshow("gray image",img2)
# to hold the image window
cv2.waitKey(0)
# to close the window
cv2.destroyAllWindows()
