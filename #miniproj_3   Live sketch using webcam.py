import cv2
import numpy as np

# our sketch generating function
def sketch(image):
    #converting image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    #clean up image using gaussian blur
    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),0)
    
    #extract edges
    canny_edges = cv2.Canny(img_gray_blur,20,70)
    
    #do an invert binarize in the image
    ret, mask = cv2.threshold(canny_edges, 70 ,255 , cv2.THRESH_BINARY_INV)
    return mask


# intialize webcam, cap is object provided by videocapture
# it contains a boolean to tell if it was successful (ret)
# it also contains images collected from webcam (frame)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('orignal live',frame)
    cv2.imshow('our live video feed',sketch(frame))
    if cv2.waitKey(1) == 13:
        break
        
cap.release()
cv2.destroyAllWindows()