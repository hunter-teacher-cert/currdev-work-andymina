import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import convolve2d

def display_image(image, title):
    """
    Display the given 2D image with a specified title.

    Parameters:
    - image: 2D numpy array representing the image.
    - title: A string title for the displayed image.
    """
    plt.figure(figsize=(3,3))
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.title(title)
    plt.xticks([])
    plt.yticks([])
    plt.show()

# Create the input data
homework_02_input = [
    [231, 221, 214, 249],
    [159, 122, 215, 120],
    [31, 22, 35, 39],
    [3, 134, 107, 131]
]

# Create the kernel
homework_02_kernel = [
    [1/9, 0, 0],
    [1/3, 1/9, 1/3],
    [0, 0, 1/9]
]

# Convolve using scipy
homework_02_result = convolve2d(
    homework_02_input, homework_02_kernel,
    mode='same', boundary='symm'
)
# Round to nearest int with numpy
homework_02_result = np.rint(homework_02_result)

print(homework_02_result)

display_image(homework_02_result, 'Result')