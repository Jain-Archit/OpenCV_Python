import cv2
import skimage
import matplotlib.pyplot as plt

image = skimage.io.imread(r"C:\Users\Sanchit\Desktop\Blog_1.jpg")
plt.imshow(image)
plt.show()
img = image[:, :, ::-1] # convert image from RGB (skimage) to BGR (opencv)
cv2.namedWindow('original', cv2.WINDOW_NORMAL)
cv2.imshow('original',img)
cv2.waitKey(0)