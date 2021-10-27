from scipy.fftpack import dct, idct
from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pylab as plt

# implement 2D DCT
def dct2(a):
    return dct(dct(a.T, norm='ortho').T, norm='ortho')

# implement 2D IDCT
def idct2(a):
    return idct(idct(a.T, norm='ortho').T, norm='ortho')    


# read lena RGB image and convert to grayscale
#
# You can use either short path or full path
# short path: fruits.jpeg
# full path: /home/arimogi/Projects/Python/Steganografi/Tugas-1/fruits.jpeg
#
#img = input("Enter image name(with extension): ")
#print("Open file: " + img)
#img = 'Lenna.jpeg'
img = 'fruits.bmp'

im = rgb2gray(imread(img))

imF = dct2(im)

im1 = idct2(imF)

# check if the reconstructed image is nearly equal to the original image
np.allclose(im, im1)
# True

# plot original and reconstructed images with matplotlib.pylab
plt.gray()
#plt.subplot(121), plt.imshow(im), plt.axis('off'), plt.title('original image', size=10)
plt.subplot(122), plt.imshow(im1), plt.axis('off'), plt.title('reconstructed image (DCT+IDCT)', size=10)
plt.subplot(221), plt.imshow(imF), plt.axis('off'), plt.title('DCT matrix', size=10)
plt.show()
