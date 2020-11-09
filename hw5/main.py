import numpy as np
import cv2

def dilation(img, kernel):
    res = np.zeros((img.shape[0], img.shape[1]), np.int)
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
                max_val = 0
                for (px, py) in kernel: 
                    new_row = row +  px
                    new_col = col + py
                    if(new_row >= 0 and new_row < img.shape[0] and new_col >= 0
                        and new_col < img.shape[1]):
                        if(img[new_row][new_col] > max_val):
                            max_val = img[new_row][new_col]
                res[row][col] = max_val
    return res

def erosion(img, kernel):
    res = np.zeros((img.shape[0], img.shape[1]), np.int)
    for row in range(img.shape[0]):
        for col in range(img.shape[1]):
            min_val = 256
            for (px, py) in kernel: 
                new_row = row +  px
                new_col = col + py
                if(new_row >= 0 and new_row < img.shape[0] and new_col >= 0
                        and new_col < img.shape[1]):
                    if(img[new_row][new_col] < min_val):
                        min_val = img[new_row][new_col]
            res[row][col] = min_val
    return res

def opening(img, kernel):
    return dilation(erosion(img, kernel), kernel)

def closing(img, kernel):
    return erosion(dilation(img, kernel), kernel)

def main():
    kernel = [(-2, -1), (-2, 0), (-2, 1), (-1, -2),(-1, -1),(-1, 0),(-1, 1), 
    (-1, 2), (0, -2), (0, -1), (0, 0), (0, 1), (0, 2), (1, -2), (1, -1), (1, 0),
    (1, 1), (1, 2), (2, -1), (2, 0), (2, 1)]
    img = cv2.imread('lena.bmp', cv2.IMREAD_UNCHANGED)
    cv2.imwrite('dilation.bmp', dilation(img, kernel))
    cv2.imwrite('erosion.bmp', erosion(img, kernel))
    cv2.imwrite('opening.bmp', opening(img, kernel))
    cv2.imwrite('closing.bmp', closing(img, kernel))

if __name__ == '__main__':
    main()