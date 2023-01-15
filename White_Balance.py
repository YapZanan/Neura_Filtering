import cv2
import numpy as np
import os
from skimage import exposure
from skimage.exposure import match_histograms

class White_Balance():
    def __init__(self):
        super().__init__()

    def grayworld(self, path, jumlah):
        """ Split gambar, average nilai, kembalikan nilai ke R G B
        https://docs.opencv.org/3.4/d7/d71/classcv_1_1xphoto_1_1GrayworldWB.html
        """

    def histogram_matching(self):
        matched = match_histograms(image, reference, channel_axis=-1)

    def retinex_adjust(nimg):
        """
        from 'Combining Gray World and Retinex Theory for Automatic White Balance in Digital Photography'
        """
        nimg = nimg.transpose(2, 0, 1).astype(np.uint32)
        sum_r = np.sum(nimg[0])
        sum_r2 = np.sum(nimg[0] ** 2)
        max_r = nimg[0].max()
        max_r2 = max_r ** 2
        sum_g = np.sum(nimg[1])
        max_g = nimg[1].max()
        coefficient = np.linalg.solve(np.array([[sum_r2, sum_r], [max_r2, max_r]]),
                                      np.array([sum_g, max_g]))
        nimg[0] = np.minimum((nimg[0] ** 2) * coefficient[0] + nimg[0] * coefficient[1], 255)
        sum_b = np.sum(nimg[1])
        sum_b2 = np.sum(nimg[1] ** 2)
        max_b = nimg[1].max()
        max_b2 = max_r ** 2
        coefficient = np.linalg.solve(np.array([[sum_b2, sum_b], [max_b2, max_b]]),
                                      np.array([sum_g, max_g]))
        nimg[1] = np.minimum((nimg[1] ** 2) * coefficient[0] + nimg[1] * coefficient[1], 255)
        return nimg.transpose(1, 2, 0).astype(np.uint8)

    def kefoto(self):
        test =  os.path.isdir("venv")
        # cv2.imwrite()
        print(test)