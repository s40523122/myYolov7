import cv2
import glob

for img in glob.glob("square/*.jpg"):
    im = cv2.imread(img)
    #im = im[:3840, :2160]
    #resize_im = cv2.resize(im, (720, 1280), interpolation=cv2.INTER_AREA)
    #resize_im = cv2.resize(im, (734, 979), interpolation=cv2.INTER_AREA)
    #resize_im = resize_im[:978, :]
    resize_im = cv2.resize(im, (1280, 1280), interpolation=cv2.INTER_AREA)
    cv2.imshow('Result', resize_im)
    cv2.waitKey(0)
    cv2.imwrite("square_1280"+img[6:], resize_im)
    #break
'''
image = cv2.imread('lena.jpg')
image = cv2.resize(image, (256, 256), interpolation=cv2.INTER_AREA)
cv2.imshow('Result', image)
cv2.waitKey(0)
'''