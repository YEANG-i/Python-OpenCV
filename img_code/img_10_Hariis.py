import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# 1 读取图像，并转换成灰度图像
img = cv.imread('img/xl_3.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 2 角点检测
# 2.1 输入图像必须是 float32
gray = np.float32(gray)

# 2.2 最后一个参数在 0.04 到 0.05 之间
dst = cv.cornerHarris(gray, 2, 3, 0.04)
# 3 设置阈值，将角点绘制出来，阈值根据图像进行选择
img[dst > 0.001 * dst.max()] = [0, 0, 255]
# 4 图像显示
plt.figure(figsize=(10, 8), dpi=100)
plt.imshow(img[:, :, ::-1]), plt.title('Harris')
plt.xticks([]), plt.yticks([])
plt.show()
