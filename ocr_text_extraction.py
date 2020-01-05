import pytesseract
import cv2
import cx_Oracle
import os


def ocr_demo():

    width = 330
    height = 135

    dim = (width, height)

    img = cv2.imread('1.jpg', cv2.IMREAD_UNCHANGED)

    gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    retval, gauss = cv2.threshold(gray_img, 40, 255, cv2.THRESH_BINARY)

    resize_img = cv2.resize(gauss, dim, interpolation=cv2.INTER_AREA)

    text = pytesseract.image_to_string(resize_img, lang='ben')

    """"cv2.imshow('show',resize_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()"""
    text = " ".join(text.splitlines())

    print(text)

    return text

