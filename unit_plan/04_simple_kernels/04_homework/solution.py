import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy.signal import convolve2d

def display_image(image):
  """
  Display the given 2D image with a specified title.

  Parameters:
  - image: 2D numpy array representing the image.
  - title: A string title for the displayed image.
  """
  plt.figure(figsize=(3,3))
  plt.imshow(image, cmap='gray', interpolation='nearest', vmin=0, vmax=255)
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

cat = read_image('cat.jpeg')
display_image(cat)

# -------------- IDENTITY KERNEL --------------

# Define the identity kernel
identity_kernel = [
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0],
]

# Perform convolution using scipy's convolve2d
identity_output = convolve2d(cat, identity_kernel, mode='same')
# Round to the nearest int
identity_output = np.rint(identity_output)
display_image(identity_output, 'Identity output')

# -------------- SHIFT KERNEL --------------

# Use numpy to quickly define a big array
shift_kernel = np.zeros((100, 100))
# Set the upper-left most pixel to one to define the shift direction
shift_kernel[0][0] = 1

shift_output = convolve2d(cat, shift_kernel, mode='same')
shift_output = np.rint(shift_output)
display_image(shift_output, 'Shift output')

# -------------- SHARPEN KERNEL --------------

sharpen_kernel = [
  [0, -1, 0],
  [-1, 5, -1],
  [0, -1, 0]
]

sharpen_output = convolve2d(cat, sharpen_kernel, mode='same')
sharpen_output = np.rint(sharpen_output)
display_image(sharpen_output, 'Sharpen output')

# -------------- BLOCK BLUR KERNEL --------------

# Use numpy to quickly define a big array
block_kernel = np.zeros((10, 10))
# Use numpy to fill the array with 1/10 since the sum of weights must be 1
block_kernel.fill(1/10)

block_output = convolve2d(cat, block_kernel, mode='same')
block_output = np.rint(block_output)
display_image(block_output, 'Block output')
