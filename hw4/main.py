import numpy as np
import cv2
import copy

def binary(img):
    midpoint = 128
    res = np.zeros((img.shape[0], img.shape[1]), np.int)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j] > midpoint:
                res[i][j] = 255
            else:
                res[i][j] = 0
    return res

def dilation(img, kernel):
    res = np.zeros((img.shape[0], img.shape[1]), np.int)
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            if(img[row][col] == 255):
                for (px, py) in kernel: 
                    new_row = row +  px
                    new_col = col + py
                    if(new_row >= 0 and new_row < img.shape[0] and new_col >= 0
                        and new_col < img.shape[1]):
                        res[new_row][new_col] = 255
    return res

def erosion(img, kernel):
    res = np.zeros((img.shape[0], img.shape[1]), np.int)
    is_eroded = True
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            for (px, py) in kernel: 
                new_row = row +  px
                new_col = col + py
                if(new_row < 0 or new_row >= img.shape[0] or new_col < 0
                    or new_col >= img.shape[1] or 
                    img[new_row][new_col] != 255):
                    is_eroded = False
            if(is_eroded):
                res[row][col] = 255
            is_eroded = True
    return res

def opening(img, kernel):
    return dilation(erosion(img, kernel), kernel)

def closing(img, kernel):
    return erosion(dilation(img, kernel), kernel)

def complement(img):
    res = np.zeros((img.shape[0], img.shape[1]), np.int)
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            if(img[row][col] == 0):
                res[row][col] = 255
            else:
                res[row][col] = 0
    return res

def hit_and_miss(img, kernel_j, kernel_k):
    complement_img = complement(img)
    img1 = erosion(img, kernel_j)
    img2 = erosion(complement_img, kernel_k)
    res = np.zeros((img.shape[0], img.shape[1]), np.int)
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            if(img1[row][col] == 255 and img2[row][col] == 255):
                res[row][col] = 255
    return res

def main():
    kernel = [(-2, -1), (-2, 0), (-2, 1), (-1, -2),(-1, -1),(-1, 0),(-1, 1), 
    (-1, 2), (0, -2), (0, -1), (0, 0), (0, 1), (0, 2), (1, -2), (1, -1), (1, 0),
    (1, 1), (1, 2), (2, -1), (2, 0), (2, 1)]
    kernel_j = [(0, 0), (0, -1), (1, 0)]
    kernel_k = [(-1, 1), (0, 1), (-1, 0)]
    img = cv2.imread('lena.bmp', cv2.IMREAD_UNCHANGED)
    img = binary(img)
    cv2.imwrite('dilation.bmp', dilation(img, kernel))
    cv2.imwrite('erosion.bmp', erosion(img, kernel))
    cv2.imwrite('opening.bmp', opening(img, kernel))
    cv2.imwrite('closing.bmp', closing(img, kernel))
    cv2.imwrite('hit-and-miss.bmp', hit_and_miss(img, kernel_j, kernel_k))


if __name__ == '__main__':
    main()