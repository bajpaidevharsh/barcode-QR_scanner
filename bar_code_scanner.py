import cv2
import numpy
from pyzbar import pyzbar



image1=cv2.imread("#location")

image1=cv2.resize(image1,(500,500))

image2=cv2.imread("location")
image2=cv2.resize(image2,(500,500))
image3=numpy.hstack((image1,image2))
code=pyzbar.decode(image3)

print(code)
cv2.imshow('output',image3)


cv2.waitKey(0)
