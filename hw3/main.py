import numpy as np
import cv2
import copy

def histogram(img):
    count = np.zeros(256, np.int)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            val = img[i][j]
            count[val] += 1
    return count

def original(img):
    np.savetxt("original_histogram.csv", histogram(img), delimiter=",")
    cv2.imwrite('original.bmp', img)

def reduced_intensity(img):
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            img[i][j] /= 3 
    np.savetxt("reduced_intensity_histogram.csv", histogram(img), delimiter=",")
    cv2.imwrite('reduced_intensity.bmp', img)

def equalization(img):
    new_pixel_list = get_new_pixel_list(img);
    total_pixels = img.shape[0] * img.shape[1] 
    for i in range(img.shape[0]):
        for j in range(img.shape[1]): 
            val = img[i][j]
            img[i][j] = 255 * np.sum(new_pixel_list[0 : val + 1]) / total_pixels
    np.savetxt("equalization_histogram.csv", histogram(img), delimiter=",")
    cv2.imwrite('equalization.bmp', img)
    
    
def get_new_pixel_list(img):
    count = np.zeros(256, np.int)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            val = img[i][j]
            count[val] += 1
    return count;


def main():
    img = cv2.imread('lena.bmp', cv2.IMREAD_UNCHANGED)
    original(img)
    reduced_intensity(img)
    equalization(img)


if __name__ == '__main__':
    main()
