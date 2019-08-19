
import numpy as np
import matplotlib.pyplot as plt


import cv2

img = cv2.imread("ipponyubi5_1.jpg",1)
img2 = cv2.imread("ipponyubi6_1.jpg",1)

#サイズ調整
img =cv2.resize(img,(600,350))
img2 =cv2.resize(img2,(600,350))

rows,cols,ch = img2.shape

M = np.float32([[1,0,0],[0,1,29]])
dst = cv2.warpAffine(img2,M,(cols,rows))

cv2.imwrite("affine.jpg", dst)


#マスク画像1の作成
black = np.full((350, 600, 1), 0, dtype=np.uint8)




# 任意の描画したいポリゴンの頂点を与える
contours = np.array([
            [37,128],
            [564,125],
            [588,216],
            [19, 215]
        ])

mask1 = cv2.fillConvexPoly(black, points =contours, color=(255, 255))

# フレーム画像とマスク画像の共通の領域を抽出する。
img_color1 = cv2.bitwise_and(img, img, mask=mask1)
cv2.imwrite("masked1.jpg", img_color1)

#マスク画像2の作成
black2 = np.full((350, 600, 1), 0, dtype=np.uint8)


# 任意の描画したいポリゴンの頂点を与える
contours2 = np.array([
            [406,182],
            [514,182],
            [514,248],
            [406,248]
        ])

mask2 = cv2.fillConvexPoly(black2, points =contours2, color=(255, 255))

# フレーム画像とマスク画像の共通の領域を抽出する。
img_color2 = cv2.bitwise_and(img2, img2, mask=mask2)
#マスク後画像を再平行移動
M = np.float32([[1,0,-4],[0,1,-22]])
img_color2 = cv2.warpAffine(img_color2,M,(cols,rows))

cv2.imwrite("masked2.jpg", img_color2)


#loop
#x
for x in range(600):
    #y
    for y in range(350):
        #ピクセルを取得
        b, g, r = img_color2[y,x]
        
        if b == 0:
            if  g == 0:
                if r == 0:
                    continue
                    
        img_color1[y, x] = img_color2[y,x]

cv2.imwrite("concat.jpg", img_color1)
####################
