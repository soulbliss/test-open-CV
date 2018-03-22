import cv2
import numpy as np



image = cv2.imread('shapes.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('Identifying shapes',image)
cv2.waitKey(0)

ret, thresh = cv2.threshold(gray, 230, 255, 1)

#extract contours
_, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

for cnt in contours:
    # get approximate polygons
    
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt,True), True)
    
    if len(approx) == 3:
        shape_name = "Triangle"
        cv2.drawContours(image,[cnt], 0, (1,5,255),-1)
        #find contour center to place text at the center
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.putText(image, shape_name, (cx-50,cy), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
    
    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(cnt)
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        
        if(abs(w-h)) <=3:
            shape_name = "Square"
            cv2.drawContours(image,[cnt], 0, (0,255,0),-1)
            cv2.putText(image, shape_name, (cx-50,cy), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
        else:
            shape_name = "Rectangle"
            cv2.drawContours(image,[cnt], 0, (155,155,255),-1)
            M = cv2.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.putText(image, shape_name, (cx-50,cy), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
            
    elif len(approx) == 5:
        shape_name = "Pentagon"
        cv2.drawContours(image,[cnt], 0, (255,0,0),-1)
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.putText(image, shape_name, (cx-50,cy), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
        
    elif len(approx) == 6:
        shape_name = "Hexagon"
        cv2.drawContours(image,[cnt], 0, (0,56,255),-1)
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.putText(image, shape_name, (cx-50,cy), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
            
    elif len(approx) == 10:
        shape_name = "Star"
        cv2.drawContours(image,[cnt], 0, (12,17,255),-1)
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.putText(image, shape_name, (cx-50,cy), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
        
    elif len(approx) >=10:
        
        shape_name ="Circle"
        cv2.drawContours(image,[cnt], 0, (200,127,255),-1)
        M = cv2.moments(cnt)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.putText(image, shape_name, (cx-50,cy), cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
        
    
        
cv2.imshow("Identified the shapes",image)
cv2.waitKey(0)


cv2.destroyAllWindows()