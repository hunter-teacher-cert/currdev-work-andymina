import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d

def display_image(image, title):
    """
    Display the given 2D image with a specified title.

    Parameters:
    - image: 2D numpy array representing the image.
    - title: A string title for the displayed image.
    """
    plt.figure(figsize=(3,3))
    plt.imshow(image.astype(np.uint8), cmap='gray', vmin=0, vmax=255)
    plt.title(title)
    plt.xticks([])
    plt.yticks([])
    plt.show()

def read_image(file_path):
    """
    Reads the image at the file path, converts it to grayscale, and returns the image as an array.

    Parameters:
    - file_path: the file path to an image

    Return:
    - The image (converted to grayscale) as an array
    """
    gray_img = Image.open(file_path).convert('L')
    return np.array(gray_img)