# openCV-Center-of-Contour
Compute the center of a contour/shape region using openCV and Python

In this Project, I am trying to compute the Center of Contour, also called centroid, for a variety of shapes that are not perfect. In other words, the shapes I am tring to compute the centroid for are human drawn that is why rectangles are not perfectly rectangle and circles are not perfectly circles and so on.

The below image illustrates this.

![shapes_and_colors](https://user-images.githubusercontent.com/87881560/145229459-b7687805-ba0b-42ab-ab6d-62ef434e8fb1.jpg)

I am going to do this in two main steps:

First, I will try to detect the outline of each shape in the image, the Contours.

Secondly, I will Compute the Center of the Contour, The Centroid.

For this, I will do the following image pre-processing:

1- convert the image to grayscale.

2- Blur the image ---> This will reduce the high frequency noise and consequently make the contour detector more accurate.

3- Binarize the Image ---> using thresholding.

The Below Image Shows The output of the project

![Screenshot from 2021-12-08 18-07-19](https://user-images.githubusercontent.com/87881560/145242504-e2c9e64b-a074-418c-b586-ee56e262dd0d.png)


