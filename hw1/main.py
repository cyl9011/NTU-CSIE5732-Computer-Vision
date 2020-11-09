import numpy as np
import cv2
from scipy import ndimage

def upside_down(img):
    return img[..., ::-1, :]

def right_side_left(img):
    return img[..., :, ::-1]

def diagonally＿flip(img):
    res = np.zeros(img.shape, np.int)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            res[i][j] = img[j][i]                            
    return res

def rotate(img):
    return ndimage.rotate(img, 45, reshape=False)

def shrink(img):
    shrinked_img = cv2.resize(img, dsize=(img.shape[0]//2, img.shape[1]//2), 
                                interpolation=cv2.INTER_CUBIC)
    res = np.zeros(img.shape, np.int);
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if(i < shrinked_img.shape[0] and j < shrinked_img.shape[1]):
                res[i][j] = shrinked_img[i][j]       
    return res

def binarize(img):
    midpoint = 128
    res = np.zeros(img.shape, np.int);
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j] > midpoint:
                res[i][j] = 255
            else:
                res[i][j] = 0
    return res

def main():
    img = cv2.imread('lena.bmp', 0)
    cv2.imwrite('1a.bmp', upside_down(img))
    cv2.imwrite('1b.bmp', right_side_left(img))
    cv2.imwrite('1c.bmp', diagonally＿flip(img))
    cv2.imwrite('2d.bmp', rotate(img))
    cv2.imwrite('2e.bmp', shrink(img))
    cv2.imwrite('2f.bmp', binarize(img))

if __name__ == '__main__':
    main()
