import cv2
import numpy as np
from PIL import Image


def get_head_image(image, head_rect):
    cv2_im = cv2.imread(image)
    rows, cols = cv2_im.shape[:2]
    pts1 = np.float32([
        [head_rect['lt']['x'] * cols, head_rect['lt']['y'] * rows],
        [head_rect['lb']['x'] * cols, head_rect['lb']['y'] * rows],
        [head_rect['rb']['x'] * cols, head_rect['rb']['y'] * rows],
        [head_rect['rt']['x'] * cols, head_rect['rt']['y'] * rows]
    ])
    pts2 = np.float32([[0, 0], [0, 230], [200, 230], [200, 0]])
    transform = cv2.getPerspectiveTransform(pts1, pts2)
    img_nparray = cv2.warpPerspective(cv2_im, transform, (200, 230))
    cv2.imwrite("img.jpg", img_nparray)
