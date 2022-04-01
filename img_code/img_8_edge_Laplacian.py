import cv2 as cv
from matplotlib import pyplot as plt

# 1 读取图像
img = cv.imread('img/xl_5.jpg', 0)
# 2 laplacian转换
result = cv.Laplacian(img, cv.CV_16S)
Scale_abs = cv.convertScaleAbs(result)
# 3 图像展示
plt.figure(figsize=(10, 8), dpi=100)
plt.subplot(121), plt.imshow(img, cmap=plt.cm.gray), plt.title('xl_5.jpg')
plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(Scale_abs, cmap=plt.cm.gray), plt.title('Laplacian_xl_5.jpg')
plt.xticks([]), plt.yticks([])
plt.show()
