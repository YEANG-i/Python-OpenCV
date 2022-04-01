# 没成功过

import cv2 as cv
from matplotlib import pyplot as plt

# 1 图像和模板读取
img = cv.imread('img/xl_7.jpg')
template = cv.imread('img/xl_7_2.jpg')
h, w, l = template.shape
# 2 模板匹配
# 2.1 模板匹配
res = cv.matchTemplate(img, template, cv.TM_CCORR)
# 2.2 返回图像中最匹配的位置，确定左上角的坐标，并将匹配位置绘制在图像上
min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
# 使用平方差时最小值为最佳匹配位置
# top_left = min_loc
top_left = max_loc
print(top_left)
bottom_right = (top_left[0] + w, top_left[1] + h)
print(bottom_right)
cv.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
# 3 图像显示
plt.imshow(img[:, :, ::-1])
plt.title('匹配结果'), plt.xticks([]), plt.yticks([])
plt.show()
