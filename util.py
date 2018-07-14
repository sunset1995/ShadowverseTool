import os
import cv2
import mss
import time
import pyautogui
import threading
import numpy as np
from PIL import Image


class ScreenShotter:
    def __init__(self, fps=30):
        '''
        Use a thread keep updating screen to shared memory
        '''
        self.spf = 1 / fps
        self.pil_img = None
        self.num_img = 0
        worker = threading.Thread(
            target=self._screenshot_worker, daemon=True
        )
        worker.start()
        while self.pil_img is None:
            time.sleep(0.3)

    def _screenshot_worker(self):
        '''
        Thread woker which keep current screenshot as
        numpy to shared memory.
        '''
        with mss.mss() as sct:
            while True:
                eps_time = time.time()

                # Get raw pixels from the first screen
                sct_img = sct.grab(sct.monitors[1])
                self.pil_img = Image.frombytes(
                    'RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX'
                )
                self.num_img += 1

                eps_time = time.time() - eps_time
                sleep_time = self.spf - eps_time
                if sleep_time > 0.001:
                    time.sleep(sleep_time)

    def get(self):
        '''
        Return current screen in 1st monitor as numpy.
        '''
        return np.array(self.pil_img)


def read_template(*path_sep):
    return np.array(Image.open(
        os.path.join(*path_sep)
    ))


def check_existed(screenshotter, temp_img, thres=0.96):
    sim = cv2.matchTemplate(
        screenshotter.get(), temp_img,
        cv2.TM_CCORR_NORMED
    )
    _, max_val, _, max_loc = cv2.minMaxLoc(sim)
    return max_val > thres


def wait(screenshotter, temp_img, mode='on', thres=0.96):
    assert(mode in ['on', 'off'])
    while True:
        existed = check_existed(screenshotter, temp_img, thres)
        if (mode == 'on' and existed) or \
            (mode == 'off' and not existed):
            return


def find_and_click(screenshotter, temp, thres=0.96, rel_w=0.5, rel_h=0.5):
    sim = cv2.matchTemplate(
        screenshotter.get(), temp,
        cv2.TM_CCORR_NORMED
    )
    _, max_val, _, max_loc = cv2.minMaxLoc(sim)
    if max_val < thres:
        return False

    x = int(round(max_loc[0] + temp.shape[1] * rel_w))
    y = int(round(max_loc[1] + temp.shape[0] * rel_h))
    pyautogui.click(x=x, y=y, interval=0.1)
    return True
