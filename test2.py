"""# Read 2 different images and create a new image by arranging them side by side
import cv2
import numpy as np

img1=cv2.imread("image/flower.jpg")
img2=cv2.imread("image/mahadev.jpg")
img1=cv2.resize(img1,(300,300))
img2=cv2.resize(img2,(300,300))


x=cv2.hconcat((img1,img2))
y=cv2.cvtColor(x,cv2.COLOR_BGR2GRAY)
print(y.shape)
print(x.shape)
#final_image=np.concatenate((x,np.expand_dims(y,axis=2)),axis=0)
cv2.imshow("final Image",y)

cv2.waitKey(0)
cv2.destroyAllWindows()"""

import cv2
import numpy as np

# Read the two images
image1 = cv2.imread('image/flower.jpg')
image2 = cv2.imread('image/mahadev.jpg')

# Ensure both images have the same height
min_height = min(image1.shape[0], image2.shape[0])
image1 = image1[:min_height]
image2 = image2[:min_height]

# Concatenate the two images side-by-side
concatenated_colored = np.concatenate((image1, image2), axis=1)

# Convert the concatenated colored image to grayscale
gray_concatenated = cv2.cvtColor(concatenated_colored, cv2.COLOR_BGR2GRAY)

# Concatenate the colored and grayscale images
final_image = np.concatenate((concatenated_colored, np.expand_dims(gray_concatenated, axis=2)), axis=0)

# Save the final image
cv2.imwrite('A1_solution.jpg', final_image)