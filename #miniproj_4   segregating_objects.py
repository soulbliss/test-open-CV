import cv2
import numpy as np

#functions we will use for sortimg by positon
'''
def x_cord_contour(contours):
    #returns the x coordinate for the contour centroid
    if cv2.contourArea(contours) > '10':
        M = cv2.moments(contours)
        if M["m00"] != 0:
        	cx = int(M["m10"] / M["m00"])
        else:
        	cx = 0
        return(cx)
 '''   
def label_contuour_center(image, c):
    #places a red circle on the centers of the contours
    M = cv2.moments(c)
    if M["m00"] != 0:
    	cx = int(M["m10"] / M["m00"])
    	cy = int(M["m01"] / M["m00"])
    else:
    	cx, cy = 0, 0

    #draw the contour number on the image
    cv2.circle(image, (cx,cy), 10, (0,0,255), -1 )
    return image


#load our image
image = cv2.imread('shapes.jpg')
orignal_image = image.copy()
cv2.imshow('orignal image',image)
cv2.waitKey(0)


#grayscale our image
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#find canny edges
edges = cv2.Canny(image,0,255)
cv2.imshow('canny edges',edges)
cv2.waitKey(0)

#find contours and print how many were found
_, contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print('Number of contours found is ',len(contours))

print(contours)        
    
#compute centre of mass or centroid and draw them on our image
for(i, c) in enumerate(contours):
    orig = label_contuour_center(image , c)

cv2.imshow('contours centres',image)
cv2.waitKey(0)
            
            

            
#labelling contours left to right
for (i, c) in enumerate(contours):
    cv2.drawContours(orignal_image, [c], -1, (0,0,255), 3)
    M = cv2.moments(c)
    if M["m00"] != 0:
    	cx = int(M["m10"] / M["m00"])
    	cy = int(M["m01"] / M["m00"])
    else:
    	cx, cy = 0, 0
    cv2.putText(orignal_image, str(i+1), (cx,cy), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255),2)
    cv2.imshow('contours centres in incres size',orignal_image)
    cv2.waitKey(0)        
    (x, y, w, h) = cv2.boundingRect(c)
    
    #lets now crop each contour and save them into images
    cropped_contour = orignal_image[y:y+h, x:x+w]
    image_name = "output_shape_number_" +str(i+1)+ ".jpg"
    print(image_name)
    cv2.imwrite(image_name,cropped_contour)
    

cv2.destroyAllWindows()