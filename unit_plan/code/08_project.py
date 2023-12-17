import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d
from IPython.display import display

def display_image(image, title=''):
    """
    Display the given 2D image with a specified title.

    Parameters:
    - image: 2D numpy array representing the image.
    - title: A string title for the displayed image.
    """
    plt.figure(figsize=(3,3))
    plt.imshow(image.astype(np.uint8), vmin=0, vmax=255)
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

def normalize_to_255(arr):
    """
    Normalize a NumPy array to be in the range [0, 255].
    """
    old_min = np.min(arr)
    old_max = np.max(arr)
    new_min = 0
    new_max = 255

    # create a new array
    normalized = np.zeros_like(arr)

    # extract the number of rows and columns
    num_rows, num_cols = arr.shape

    for row in range(num_rows):
        for col in range(num_cols):
            # if we're going to divide by 0, just insert 0
            if (old_max - old_min == 0):
                normalized[row][col] = 0
            else:
                # formula taken from L4, S3
                fraction = (arr[row][col] - old_min) / (old_max - old_min)
                normalized[row][col] = fraction * (new_max - new_min) + new_min

    # round to nearest int with numpy
    return np.rint(normalized)

def detect_edges(img, x_kernel, y_kernel):
    """
    Detect edges in an image using convolution with custom x and y kernels.

    Parameters:
    - img: The input image (2D array) to detect edges in.
    - x_kernel: The convolution kernel for detecting edges in the x-direction.
    - y_kernel: The convolution kernel for detecting edges in the y-direction.

    Returns:
    - An array representing the magnitude of edges detected in the input image.
      The result is computed as the absolute magnitude of the convolution results using the x and y kernels.

    Note:
    - The convolution is performed in 'same' mode to ensure the output has the same dimensions as the input image.
    - The magnitude of edges is calculated as the square root of the sum of squared x and y edge responses.
    """
    x_edges = convolve2d(img, x_kernel, mode='same') 
    y_edges = convolve2d(img, y_kernel, mode='same')
    res = np.sqrt(x_edges**2 + y_edges**2)
    res = normalize_to_255(res)
    return res

def prewitt_edge_detector(img):
    # define prewitt x and y kernels
    prewitt_x = [
        [-1, 0, 1],
        [-1, 0, 1],
        [-1, 0, 1]
    ]

    prewitt_y = [
        [1, 1, 1],
        [0, 0, 0],
        [-1, -1, -1]
    ]

    return detect_edges(img, prewitt_x, prewitt_y)

def sobel_edge_detector(img):
    sobel_x = [
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]
    
    sobel_y = [
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]
    ]

    return detect_edges(img, sobel_x, sobel_y)

def scharr_edge_detector(img):
    scharr_x = [
        [-3, 0, 3],
        [-10, 0, 10],
        [-3, 0, 3]
    ]
    
    scharr_y = [
        [3, 10, 3],
        [0, 0, 0],
        [-3, -10, -3]
    ]

    return detect_edges(img, scharr_x, scharr_y)

def recolor_image(edge_img, bg_color, fg_color):
    num_rows, num_cols = edge_img.shape
    result = np.zeros((num_rows, num_cols, 3))
    
    for row in range(num_rows):
        for col in range(num_cols):
            edge_val = edge_img[row][col]

            # absolutely not an edge here
            if edge_val == 0:
                # full intensity on the bg color
                result[row][col] = bg_color
            # definitely an edge here
            else:
                # use the edge intensity to determine transparency
                result[row][col] = alpha_blend(fg_color, bg_color, edge_val)

    return result

def alpha_blend(fg_color, bg_color, fg_intensity):
    alpha = fg_intensity / 255
    color = alpha * np.array(fg_color) + (1 - alpha) * np.array(bg_color)
    return color

def get_rgb():
    r = int(input('Enter red value 0-255: '))
    g = int(input('Enter red value 0-255: '))
    b = int(input('Enter red value 0-255: '))
    return [r, g, b]

def make_line_art(img, kernel_type, fg_color, bg_color):
    if kernel_type == 'Prewitt':
        edge_img = prewitt_edge_detector(img)
    elif kernel_type == 'Sobel':
        edge_img = sobel_edge_detector(img)
    else:
        edge_img = scharr_edge_detector(img)

    line_art = recolor_image(edge_img, fg_color, bg_color)
    return line_art

img = read_image(input('Enter file path: ')) # for example, images/shapes.png
kernel_type = input('Enter kernel (Prewitt, Sobel, Scharr): ')

# get foreground rgb color
print('Foreground color')
fg_color = get_rgb()

# get background rgb color
print('Background color')
bg_color = get_rgb()

line_art = make_line_art(img, kernel_type, fg_color, bg_color)
display_image(line_art, 'Result')