import numpy as np
import matplotlib.pyplot as plt

def display_image(image, title=''):
    """
    Display the given 2D image with a specified title.

    Parameters:
    - image: 2D numpy array representing the image.
    - title: A string title for the displayed image.
    """
    plt.figure(figsize=(3,3))
    plt.imshow(image, cmap='gray', interpolation='nearest')
    plt.title(title)
    plt.xticks([])
    plt.yticks([])
    plt.show()

def create_gaussian(size, sigma = None):
    """
    Create a simple 2D square Gaussian distribution.

    Parameters:
    - size: Integer specifying the size of the output square array (height and width are the same).
    - sigma: Standard deviation of the Gaussian.

    Returns:
    - A 2D NumPy array representing the square Gaussian distribution.
    """
    if sigma == None:
      sigma = size / 5

    # Create an empty kernel
    gaussian = np.zeros((size, size))

    # Calculate the center of the kernel.
    # The kernel is square so the center is the same for the row and col
    center = size // 2

    # The Gaussian is a function of the x,y or col, row. Each col,row combination
    # produces the Gaussian value at that point.
    for row in range(size):
        for col in range(size):
            # Squared distance from this point to the center.
            d = (row - center)**2 + (col - center)**2

            # Set up the exponent
            exponent = (- 1 / (2 * sigma**2)) * d

            # G(col, row) = e^(exponent)
            gaussian[row][col] = np.exp(exponent)

    # Normalize to make sure the sum is 1
    return gaussian / np.sum(gaussian)

size = 15  # Size of the square Gaussian
sigma = 3  # Standard deviation of the Gaussian

gaussian = create_gaussian(size, sigma)

display_image(gaussian, 'Gaussian Kernel (size=15, sigma=3)')