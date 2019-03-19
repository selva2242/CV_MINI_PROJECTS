import cv2






def sketch(image):
    #change to gray_scale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #cleanup image
    Guassian_image = cv2.GaussianBlur(gray_image, (5,5), 0)

    #edge detection
    canny_edges = cv2.Canny(Guassian_image, 10, 70)

    #inverting
    ret, mask = cv2.threshold(canny_edges, 70, 255, cv2.THRESH_BINARY_INV)
    return mask

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow('selva',sketch(frame))
    if cv2.waitKey(1)==13:
        break

cv2.destroyAllWindows()
cap.release()

