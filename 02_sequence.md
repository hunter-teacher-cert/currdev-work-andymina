# 2D Computer Vision Curriculum

## Unit Sequence

**Prereqs**: AP CS A, AP Calc
**Grade Level**: 12

### Unit 1 - Introduction to 2D images

- how 2d images are formed and read in computers

### Unit 2 - Processing Binary Images

- work only with black and white images.
- can calculate physics info about objects in the img

### Unit 3 - Convolutions and Filtering

- learn what convolutions are and how to apply them.
- how they can be used in image modification

### Unit 4 - Shape Detection

- edge detection with sobel/laplace filters
- line detection with hough transform
- corner detection

### Unit 5 - ML/AI in Computer Vision

- convolutional neural networks
- face detection/recognition
- object recognition
- ethics of computer vision

## Explanation

I think Unit 1 is pretty self-explanatory for going first, but I do think it's worth noting that
Unit 1 is mostly pen and paper math. There isn't a lot of programming of student-computer interaction
in this unit so students can get a strong foundation of how images are formed (i.e. pinhole camera
and light reflections) and how they're read in computers (i.e. a `m x n` 3 dimensional array). The
pen-and-paper vs. programming split would be about 80%/20% or maybe even 90%/10% where the smaller
portion is mainly to prepare students for a complex programming course.

This leads into Unit 2 where students work with the simplest form of images, binary, where pixels are
black or white. The crux of this unit is object identification and is also the hardest part. Object
identification requires a disjoint-union dataset and while I can provide students with the code, I'm
not sure how to abstract it into simpler terms for students when they code this up.

After learning about binary images in Unit 2, students work with grayscale images in Unit 3 and do
basic imagine editing. Convolutions are the emphasis in this unit as they will set the scene for
Units 4 and 5. This unit is more about introducing convolutions then how they work. The primary mode
of student assignments will be pen and paper again, but students will do more programming than they
did in Unit 1. The pen-and-paper vs. programming split would be about 60%/40%.

Unit 4 directly builds off of the work done in Unit 3 as this unit is all about applying more
convolutions to images to infer information. The Sobel and LaPlace filters can calculate the derivative
from which one can infer edges in the images. The material covered in this unit isn't focused on practicing
working with convolutions but moreso making inferences and extracting data using convolutions.

Unit 5 is the final unit where students use what they've learned to understand the larger field
of computer vision that permeates their lives already. I think ethics in computer vision is extremely
important as it tends to be the subfield that leans most *unethically* which is why I included it.
This would be a more pen-and-paper and discussion heavy unit rather than programming. The split would
be around 70%/30%.

