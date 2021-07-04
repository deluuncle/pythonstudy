import os
import cv2
import numpy as np


def sliding_window(image,mask_image,step_size,window_size,height,width,count):
    for y in range(0,image.shape[0],step_size):
        if