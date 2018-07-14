import os
import cv2
import time
import PIL.Image as Image
import numpy as np

import util

# Create sceen reader (using another thread)
screenshotter = util.ScreenShotter()

img_template = Image.open(os.path.join('templates', '2pick', 'arena.png'))
img_template = np.array(img_template)

s_time = time.time()
for i in range(10000):
    img_screen = screenshotter.get()
    print(img_screen.dtype, img_screen.min(), img_screen.max())
    print(img_template.dtype, img_template.min(), img_template.max())
    diff = cv2.matchTemplate(img_screen, img_template, cv2.TM_CCORR_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(diff)

    fps = (i + 1) / (time.time() - s_time)
    print('FPS: %2f / max_val: %.6f' % (fps, max_val))
