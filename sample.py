import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pickle
import cv2

# path = 'original/2020-06-05_17.00_no.jpg'
# image = mpimg.imread(path)
# ax = plt.gca()
# ax.set_xticks(np.arange(0, 1280, 50));
# ax.set_yticks(np.arange(0, 800, 50));
# ax.set_xticklabels(np.arange(0, 1280, 50));
# ax.set_yticklabels(np.arange(0, 800, 50));
# plt.imshow(image)
# #plt.setp(plt.gca(), autoscale_on=False)
# plt.show()


path = r'original/2020-06-05_17.00_no.jpg'
img = cv2.imread(path)

# cv2.imshow('sample', img)
crop_img = img[600:800, 550:600]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)
# if cmd == ord('1'):
#     break
#     elif cmd == 32: # space
#         print('whatever')
#         continue
#     elif cmd == 27: # ESC
#         break