import cv2


img = cv2.imread('assets/pexels-paul-ijsendoorn-1181202.jpg',1)

# .Canny algo to utilize cv2 edge detection capabilities
edge = cv2.Canny(img, 0, 200)

edge_edit = cv2.resize(edge, ( 400, 400))

cv2.imshow('edged',edge_edit)

key = cv2.waitKey(0)

if key == ord('q'):
    cv2.destroyAllWindows()
