# Worksheet - Converting from RGB to Grayscale

Sometimes it's necessary to convert RGB images to Grayscale to make them easier to work with. For
example, 200x300 RGB image has 180,000 pieces of information (200 columns &times; 300 rows &times;
3 color values per pixel), but a Grayscale image of the same size only has 60,000.

This worksheet should be done in pairs, but each students should have their own copy.

## Review of Color Models

1. In 2-3 sentences describe the difference between the RGB color model and the Grayscale color model.
    > <br/>
    > <br/>
    > <br/>

2. Write down five RGB color combinations and the colors they produce.

    1. ______ = `rgb(____, ____, ____,)`
    2. ______ = `rgb(____, ____, ____,)`
    3. ______ = `rgb(____, ____, ____,)`
    4. ______ = `rgb(____, ____, ____,)`
    5. ______ = `rgb(____, ____, ____,)`

3. Is it ever possible to get pink using a Grayscale color model? Circle one: Yes or No.
    - If so, write down the gray value. `gray(_____)`

4. True or False? The RGB AND Grayscale color models are both additive color models. _____

## Simple Conversion Algorithm

As we learned in the "Color Models in Computer Images" Lab, if the RGB values are all equal, we
can easily use one of the values as a gray value in the Grayscale color model. However, when they
aren't equal, one of the simpler conversion algorithms is to average the red, green, and blue values.

Complete the following questions and discuss your answers with a neighboring group.

1. Convert the following RGB colors to Grayscale using the simple conversion algorithm. Show your work.
    1. `rgb(255, 128, 4)` = `gray(_____)`
    2. `rgb(40, 56, 255)` = `gray(_____)`
    3. `rgb(38, 182, 201)` = `gray(_____)`

2. Write a static method that takes in the red, green, and blue values of a pixel
and returns the associated gray value.

```java
// STUDENT ANSWER
public static int simpleConvertToGray(int red, int green, int blue) {
    // NOTE: we're not using a double here since the only possible gray values are from 0-255.
    int average = (red + green + blue) / 3;
    return average;
}
```

### Simple Conversion in Action

Consider this image of leaf in RGB format.

![image of leaf](https://www.tutorialspoint.com/dip/images/rgb.jpg)

If we convert this image using our simple algorithm by looping over each pixel and setting its
gray value to the average of the red, green, and blue values, we will get:

![simple grayscale leaf](https://www.tutorialspoint.com/dip/images/rgb_gray.jpg)

## NTSC Conversion Algorithm

While the simple conversion algorithm works, you may have noticed that our grayscale leaf has turned
out particularly dark. A lot of the brightness and shading in the original image has been lost. This
is because our eyes don't perceive all colors at equal intensity. We perceive green more intensely
than we do red and red more intensely than we do blue. Below are the proportions/weights we perceive
these colors at with our eyes:

- red at 0.30 intensity
- green at 0.59 intensity
- blue at 0.11 intensity

The NTSC conversion algorithm uses these weights when converting to give a better sense of brightness
and tone in Grayscale images.

Complete the following questions and discuss your answers with a neighboring group.

1. Using the color weights above, convert the following RGB colors to Grayscale. Show your work.
    1. `rgb(255, 128, 4)` = `gray(_____)`
    2. `rgb(40, 56, 255)` = `gray(_____)`
    3. `rgb(38, 182, 201)` = `gray(_____)`

2. Write a static method that takes in the red, green, and blue values of a pixel
and returns the associated gray value using a weighted average.

```java
// STUDENT ANSWER
public static int NTSCConvertToGray(int red, int green, int blue) {
    // NOTE: we use doubles here to get an accurate average later
    double weightedRed = 0.30 * red;
    double weightedGreen = 0.59 * green;
    double weightedBlue = 0.11 * blue;

    int average = (weightedRed + weightedGreen + weightedBlue) / 3;
    return average;
}
```

Using the NTSC conversion and weighted averages, our original leaf would look like

![NTSC grayscale leaf](https://www.tutorialspoint.com/dip/images/weighted_gray.jpg)
