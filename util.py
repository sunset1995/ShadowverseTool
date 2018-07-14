import mss
import time
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
