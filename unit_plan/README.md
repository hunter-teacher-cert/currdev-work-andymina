# Edge Detection with Convolution

by Andy Mina

**Course**: Introduction to Computer Vision

**Grade level**: 11-12th grade

## Course background

### Prerequisites

The "Introduction to Computer Vision" course is only offered to students who have already taken AP Computer Science A in Java. While not necessary, it would be beneficial if students have also taken one of the following classes:

- Introduction to Python
- Matrix Algebra
- Calculus (AB or BC)

### Description

In this course, students will gain a deeper understanding of how computers receive, process, and manipulate input "visual data." Students will create their own implementations of modern computer vision algorithms used in widely popular technologies and tools such as blurring an image, extracting the average "color(s)" from an image, and basic object detection. At the end of the course, students will be required to research and write a brief report explaining recent work in an area of interest within the computer vision field. After this course, students will walk away with a deeper understanding of how computer vision technology permeates the world around them and a portfolio of projects to further prove their findings. The unit sequence for this course is:

- How human vision works
- Introduction to Python and NumPy-
- Image processing
  - Images as 2D arrays
  - Color models and channels
- Binary images
  - Object counting and segmentation
  - Object physics and properties
- Edge detection with convolution
- Corner detection
- Template matching
- Canny Hough edge fitting
- Hough transform for line fitting
- Stereo images
  - Shape from structure
- Artificial Intelligence and Machine Learning
  - Convolution neural networks
  - Neural networks
  - Face detection/recognition
  - Ethics of AI/ML
- Student research project

### Motivation for Course

I personally find the field of computer vision extremely interesting. I find it fascinating that many of us take the tools we use daily for granted. Even the process of taking an image is so unbelievably complex and I would love for students to develop a deeper appreciation for commonly used tools like Photoshop for image editing and DALL-E for image generation by understanding the fundamentals and beginning of computer vision.

As I've mentioned before, I have some CS education experience, mainly in teaching web development. I'd like to steer away from web development as a potential course to try something new and continue building my teaching portfolio. I've taken a computer vision course at Hunter College in my undergrad so this project presented the opportunity to digest collegiate matieral into a high-school friendly form.

---

## Unit background

### General Overview

As referenced in the unit sequence above, this unit is around the middle of the course. By this point, students should be comfortable with basic Python programming (variables, loops, conditionals, functions, and packages) and familiar with NumPy. This unit introduces convolution as a form of data extraction and image editing in the first week and then applies convolution to edge detection. The first week of this unit doesn't have much programming to it since we're mainly going into the theory of convolution and edge detection. Once the foundations are established in this unit, later units like Template matching and Canny Hough edge fitting are very programming heavy.

---

### Motivation for Unit

I think convolution is extremely cool with very interesting discussion surrounding it. Similar to how pi always ends up appearing in almost all math problems, convolution appears in the areas you least expect. Most of the key computer vision operations and features are based on convolution. In addition, convolution and edge detection, as opposed to the other topics, offer the best opportunity to discover some of the material on their own. In this unit, students are encouraged to come up with kernels based on the material they've seen already to solve new problems.

#### Unit Design

The root `unit_plan/` folder follows the specification for the project, but there's also a `daily/` folder that more closely mirrors how an instructor would deliver this unit. The structure of the `daily/` folder is:

```plaintext
daily/
  ├─ xx_lesson/ (i.e. 00_intro)
    ├─ xx_homework/
    │  ├─ solution.pdf
    │  └─ student.pdf
    ├─ lesson_plan.pdf
    ├─ slides.pdf
    └─ README.md (contains links to Google Docs and Slides)
```

Lesson with code-along components also have two files (`xx_instructor.ipynb` and `xx_student.ipynb`). The first is an instructor aid with completed code and the second is to be distributed to students.

The unit is meant to be delievered in a format where students have access to the slides on the day of class and the instructor uses the lesson plan alongside the slides. This means instructors should have both the slides open for class presentation and the lesson plan open for themself.

---

### Standards Referenced

- 9-12.CT.2 - Computational Thinking, Data Analysis and Visualization
- 9-12.CT.3 - Computational Thinking, Data Analysis and Visualization
- 9-12.CT.4 - Computational Thinking, Abstraction and Decompisition
- 9-12.CT.5 - Computational Thinking, Abstraction and Decompisition
- 9-12.CT.6 - Computational Thinking, Algorithms and Programming
- 9-12.CT.8 - Computational Thinking, Algorithms and Programming
- 9-12.CT.9 - Computational Thinking, Algorithms and Programming
- 9-12.CT.10 - Computationl Thinking, Algorithms and Programming
- 9-12.DL.2 - Digital Literacy, Digital Use

---

### Tools Used

- Python
  - This course uses Python since it's simpler for high-level concepts like convolution and the easy to abstract away the low-level programming details. The goal is for students to know how these features in computer vision work fundamentally; the code is just a tool for that understanding.
  - Python also has a great resource of computer vision tools easily available, most notably [OpenCV](https://docs.opencv.org/3.4/d6/d00/tutorial_py_root.html) which would be used in later units and the final project.
- [NumPy](https://numpy.org/)
  - NumPy provides tons of convenience methods for working with large arrays that are useful for computer vision (and data science if students choose to later explore that). Creating 3D arrays for RGB images, doing math on complex arrays (adding two 2D arrays together), or normalizing array values is all extremely easy with NumPy.
- [Matplotlib](https://matplotlib.org/) and [Pillow](https://python-pillow.org/)
  - Helper tools used during this course for loading images as arrays and displaying arrays as images. Not the focus of the course, but helpful nonetheless.
- [Jupyter Notebook](https://jupyter.org/)
  - Similar to Google CoLab, Jupyter Notebook is a tool that allows students to write notes in Markdown and code in Python in the same file. If students take notes, they're strongly encouraged to do using Jupyter Notebook. Code alongs are delivered using Jupyter Notebook so students can reference the code and recreate the code along themselves.

---

### Resources

There are class slides to be used every lesson in `resources/slides/`. The slides function as notes for the students so they can spend less time taking notes and more time asking questions. Students are more than welcome to take notes during the class, but since the class is mainly project-based, deeply understanding the material is more important than memorizing it. The slides have been designed to be descriptive and visual enough so students can go back on their own and review the lesson if necessary.

The lesson slides include links to the two 3Blue1Brown videos used, but students are encouraged to check out the resources below for extra review, however it should be noted that the material is complex and high-level.

- [First Principles of Computer Vision - Edge detection](https://www.youtube.com/watch?v=7AlwDYmjrcs&list=PL2zRqk16wsdqXEMpHrc4Qnb5rA1Cylrhx)
  - This channel run by Prof. Shree Nayar at Columbia is a haven of computer vision material. This specific video talks about the edge detection material covered in Week 01, but student can watch other videos.
- [But what is a convolution?](https://www.youtube.com/watch?v=KuXjwB4LzSA)
  - 3Blue1Brown is always a great resource for students to check out in breaking down high-level math into easy-to-digest visual proofs. This specific videos rediscovers edge detection using first-derivative kernels.

---

## Lessons

Total length: 2 Weeks

### Week 00 - Introduction to Convolution

- 00_intro
  - Students are introduced to 1D convolution as a mean of extracting data from a list of numbers.
- 01_2d_convolution
  - Students translate their knowledge about 1D convolution into 2D with some simple examples.
- 02_practice
  - Students work on three 2D convolution problems: first as a class, then in pairs, and finally on their own. This lesson is meant to get students comfortable with 2D convolution since it's the foundation for the following lessons.
- 03_code
  - Code along lesson where students translate the 2D convolution problems they worked on in 02_practice into code in a similar fashion: first as a class, then in pairs, and finally on their own.
- 04_simple_kernels
  - Students learn how 2D convolution can be a form of image manipulation and editing. This lesson features four simple kernels: identity, shift, block blur, and sharpen.

### Week 2 - Advanced Convolutions

- 05_gaussian
  - Students are introduced to the Gaussian distribution (1D and 2D) and learn how the Gaussian distribution create a convolution kernel that's useful everywhere.
- 06_edge_detection
  - Students are introduced to the basic theory of edge detector which uses a combination of convolution and derivatives to measure the rate of change in pixel intensity/brightness in a small region. In this lesson, students derive the Prewitt edge detector from their knowledge about the block blur kernel.
- 07_comparing_edge_detectors
  - Students learn about another edge detection kernel, the Sobel operator, and compare and constrast the differences between it and the Prewitt operator.
- 08_project
  - Students work on a sumamtive project in pairs that generates a line art image from a source image using edge detection. Students are strongly encouraged to reference old slides, code alongs, and homeworks as this project uses most of the same material.
- 09_test
  - Students continue working on the line art generator project.

---

## Assesments

### Formative

#### Homework

Students are assigned homework in a handful of lessons, all in `resources/assignments/`:

- 00_intro: Students work on two 1D convolution problems
- 02_practice: Students work on one 2D convolution problem.
- 03_code: Students translate 02_practice homework into code.
- 04_simple_kernels: Students code up image manipulation using convolution for the four simple kernels covered in class.
- 05_gaussian: Students write a method that creates a 2D square Gaussian kernel.

#### Roll for Confidence

Students will be asked to “roll for confidence” and respond by showing the instructor a number from 1 to 5 on one of their hands. Their confidence is representative of how comfortable they feel in continuing to explore and compare other sorting algorithms on their own. Scores represent the following:

1. Not confident. Needs a re-explanation or summary of the lesson with emphasis on key points.
2. Pretty shaky. Needs a brief recap and some teacher-guided practice to solidify concepts and understanding.
3. Okay. Needs some peer-guided practice and some more time to let things sink in. Ideal rating after the lesson.
4. Pretty confident. Needs some peer-guided practice for more challenging algorithms, but is self-sufficient for what’s covered in class. Ideal rating before a unit test.
5. Extremely confident. Needs little to no guidance and can tackle problems of exceptional difficulty with relative ease. Indicative of an under-challenged student.
These checks shouldn’t take any longer than one minute.

### Summative

#### Line Art Generator Project

Students are assigned this project to work in pairs. This project is a summative assessment that is the culmination of everything they have studied thus far regarding convolution and edge detection. The project description is in `resources/assignments/`.
