# Lab - Color Models in Computer Images

The internet is filled with images. From cyber-journalism to memes, images permeate every sphere
of our online sphere. This lab will give you a better understanding of how these images are represented
in code on the websites you visit and texts you send.

## Section 1 - How do we describe images?

When we talk about an image size in real-life, the first number is the width and the second number
is the height. In code, we generally think of images as two-dimensional lists where each element
in this list is a pixel.

*Answer*: For 1920x1080 sized image, fill in the blanks describing the size and shape of the
two-dimensional array repsenting this image in code.

- ____ rows
- ____ columns
- ____ elements

### What's the difference between image file types?

Images can come in many different formats which different **extensions** representing a file type.
You may have seen file types like `.JPG` and `.PNG` before. `.PNG` file types offer better quality
and even transparency, but are usually larger in file size. `.JPG` file types have reduced quality
and suffer from image compression, but are extremely smaller in file size.
On Google Images, you can search for images with specific file types.

*Answer*: Which of the following choices is not an image file type? ____

*Hint*: Feel free to use Google...

1. `.JPG2000`
2. `.RGB`
3. `.TIFF`
4. `.PGM`
5. `.GIF` (however you pronounce it)

### What makes up an image?

Computer images are made up of smaller, atomic units called **pixels**. For a computer image, the pixel
is the smallest subdivision we can reach. Depending on the type of image, a pixel may contain
different data. The information for a pixel can be different depending on the image's **color space**.

## Section 2 - The RGB Color Model

Image file types like `.JPG` and `.PNG`, use an **Red-Green-Blue (RGB) color model**. In the RGB color
model, a pixel holds three values, each ranging from 0-255, the determines how much of a certain color
the pixel should have. You can imagine the "amount" of color as a scale from 0 - 100%; 255 red means
we use 100% of the red available and, conversely, 0 blue means we use 0% of the blue available.

*Answer*: If 0 in RGB format represents 0% and 255 in RGB format represents 100%, what RGB number
would represent:

- 25%? ____
- 50%? ____
- 75%? ____

The RGB color model is **additive color model** meaning all colors can be made as a combination of
red, green, and blue. The addition of all colors would give white and the removal of all colors
would give black. This **additive color model** mainly exists in digital mediums and light refactions.
For simplicity, we will notate an RGB color with an imaginary RGB method:
`rgb(RED_VALUE, GREEN_VALUE,BLUE_VALUE)`.

This differs from the **subtractive color model** we see in printed media where colors are created
by removing certain tones. Consider printing out an image: removing all colors would produce white
and adding all colors would make black.

*Answer*: Without using an external aid, describe in simple terms what colors the
following RGB combinations would make.

- ______ = `rgb(255, 0, 0)`
- ______ = `rgb(0, 255, 0)`
- ______ = `rgb(0, 0, 255)`
- ______ = `rgb(0, 0, 0)`
- ______ = `rgb(255, 255, 255)`

*Answer*: Using an external aid (maybe [Google's RGB color picker](https://g.co/kgs/752LXz)?),
describe in simple terms what colors describe in simple terms what colors the following
RGB combinations would make.

- ______ = `rgb(255, 255, 0)`
- ______ = `rgb(255, 0, 255)`
- ______ = `rgb(0, 255, 255)`
- ______ = `rgb(0, 255, 128)`
- ______ = `rgb(128, 128, 128)`

*Answer*: Find three more RGB combinations and write below their RGB values and the color they would
display.

1. ______ = `rgb(____, ____, ____,)`
2. ______ = `rgb(____, ____, ____,)`
3. ______ = `rgb(____, ____, ____,)`

## Section 3 - The Grayscale Color Model

In Section 2, you may have noticed when the red, green, and blue values are all equal we get one of
three colors:

1. `red == green == blue == 0` gives black
2. `red == green == blue == 255` gives white
3. `red == green == blue == 128` gives gray

When the red, green, and blue values are equal, we can simplify and use the **Grayscale color model**.
Image file types like `.PGM` exclusively use the Grayscale color model.

Similar to the RGB color model, the amount of color can only range from 0-255. The value represents
the amount of gray to be displayed. For simplicity, we will notate a Grayscale color with
an imaginary method: `gray(GRAY_VALUE)`.

*Answer*: Without using an external aid, describe in simple terms what colors the
following Grayscale colors would make.

- ______ = `gray(0)`
- ______ = `gray(255)`
- ______ = `gray(128)`

*Answer*: Come up with three more Grayscale colors and rank them in terms of brightness.

1. `gray(_____)`
2. `gray(_____)`
3. `gray(_____)`
