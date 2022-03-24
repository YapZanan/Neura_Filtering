import cv2
import numpy
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

    def kefoto(self):
        test =  os.path.isdir("venv")
        # cv2.imwrite()
        print(test)