import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 1 读取图像
img = cv.imread('img/xl_1.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 2 sift关键点检测
# 2.1 实例化sift对象
sift = cv.xfeatures2d.SIFT_create()

# 2.2 关键点检测：kp关键点信息包括方向，尺度，位置信息，des是关键点的描述符
kp, des = sift.detectAndCompute(gray, None)
# 2.3 在图像上绘制关键点的检测结果
cv.drawKeypoints(img, kp, img, flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# 3 图像显示
plt.figure(figsize=(8, 6), dpi=100)
plt.imshow(img[:, :, ::-1]), plt.title('sift检测')
plt.xticks([]), plt.yticks([])
plt.show()
