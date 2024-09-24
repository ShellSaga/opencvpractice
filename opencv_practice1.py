import cv2

img = cv2.imread('assets/wallhaven-481e7y.jpg',1)
# img =cv2.resize(variable_name, height,width) resizes the image
img = cv2.resize(img,(550, 350))
# img = cv2.rotate(variable_name, cv2.cv2.rotate_90_clockwise) rotates the image



blackwhite = cv2.imread('assets/wallhaven-481e7y.jpg',0)
blackwhite = cv2.resize(blackwhite,(0,0),fx= 0.5, fy= 0.5)


# .copy is used to copy the image
rectangleimg = blackwhite.copy()

# cvs.Rectangle(variable name, dimensions of rectangle desired)
cv2.rectangle(rectangleimg, (50,50), (200,200),(0,0,255), 2)

#  to view the image
cv2.imshow('Rectangle',rectangleimg)

# to save the new edited image as a new file
cv2.imwrite('edited_img.jpg', blackwhite)

if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()

