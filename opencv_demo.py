import cv2


def cv_demo():

    cam = cv2.VideoCapture(0)

    cv2.namedWindow("Camera")

    ic = 0

    while True:
        ret, frame = cam.read()
        cv2.imshow("Camera", frame)
        if not ret:
            break
        k = cv2.waitKey(1)

        if k%256 == 27:
            # if ESC is pressed, break the loop
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # if SPACE is pressed ,take a photo
            img_name = "Image_{}.png".format(ic)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            ic += 1

    cam.release()
    cv2.destroyAllWindows()
    return img_name
