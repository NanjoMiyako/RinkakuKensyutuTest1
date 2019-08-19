
import numpy as np
import matplotlib.pyplot as plt
import cv2
import random




def detect_contour(img, out_img, min_size):


    # detect contour
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour_num = 0
    crops = []
    # draw contour
    for c in contours:
        #print(cv2.contourArea(c))
        
        if cv2.contourArea(c) < min_size:
            continue
        contour_num = contour_num + 1
        
        # rectangle area
        x, y, w, h = cv2.boundingRect(c)
        x, y, w, h = padding_position(x, y, w, h, 5)

        #20区分に分けて乱数値で輪郭の色を設定
        green = (random.uniform(0.0, 20.0) * 12.7)
        blue = (random.uniform(0.0, 20.0) * 12.7)
        red = (random.uniform(0.0, 20.0) * 12.7)
        
        # draw contour
        cv2.drawContours(img_out, c, -1, (0, 0, 255), 3)  # contour
        cv2.rectangle(img_out, (x, y), (x + w, y + h), (green, blue, red), 3)  #rectangle contour

    print(contour_num)
    return img_out


def padding_position(x, y, w, h, p):
    return x - p, y - p, w + p * 2, h + p * 2

###以降メイン処理###

img = cv2.imread("concat.jpg",1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("img_gray.jpg", gray)

gray2 = cv2.bitwise_not(gray)
cv2.imwrite("img_gray2.jpg", gray2)

# 閾値の設定
threshold = 80

# 二値化(閾値100を超えた画素を255にする。)
ret, gray3 = cv2.threshold(gray2, threshold, 255, cv2.THRESH_BINARY)
gray3 = cv2.bitwise_not(gray3)
cv2.imwrite("img_gray3.jpg", gray3)

img_out = cv2.imread("white.jpg",3)
min_size = 30
# 輪郭検出
image, contours = cv2.findContours(
    gray3, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
img2 = detect_contour(gray3,img_out,500)

cv2.imwrite("img_contour.jpg", img2)
