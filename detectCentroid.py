import cv2

# Loading The image
image = cv2.imread('shapes_and_colors.jpg')
# Visualize The Image
## cv2.imshow("Image", image)
## cv2.waitKey(0)
# Convert Image to Grayscale
gimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Visualize The Grayscale Image
## cv2.imshow("Grayscale Image", gimage)
## cv2.waitKey(0)
# Blurring The Image
bimage = cv2.GaussianBlur(gimage, (5, 5), 0)
# Visualize The Blurred Image
## cv2.imshow("Blurred Image", bimage)
## cv2.waitKey(0)
# Binarizing The Image Using Thresholding
(T, timage) = cv2.threshold(bimage, 60, 255, cv2.THRESH_BINARY)
# Visualize The Binarized Image
## cv2.imshow("Binarized Image", timage)
## cv2.waitKey(0)
# After Applying Thresholding The Shapes in the image are presented as a white foreground on a black background
# Using The Black and White Image We Will Try to Find The Locations of The White Regions, Shapes, using Contour Detection
(cnts, _) = cv2.findContours(timage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Now We can Visualize the Contours
## contourImage = image.copy()
## cv2.drawContours(contourImage, cnts, -1, (255, 255, 255), 2)
## cv2.imshow("Image With Contours", contourImage)
## cv2.waitKey(0)

# Now That we have computed the Contours, We are ready to process each one of them and calculate its centroid
e = 10e-6       # To Avoid the Division by Zero
for c in cnts:
    # First we will calculate the region moment, weighted average of the pixels
    M = cv2.moments(c)
    # Calculate the Centroid
    CX = int(M['m10'] / (M['m00'] + e))
    CY = int(M['m01'] / (M['m00'] + e))
    # Draw The Contours
    cv2.drawContours(image, [c], -1, (255, 255, 255), 2)
    # Draw the Centroids
    cv2.circle(image, (CX, CY), 7, (255, 255, 255), -1)
    # Writing the Word "Center" near the Centroids detected
    cv2.putText(image, 'Center', (CX - 20, CY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

cv2.imshow("Detected Centroids", image)
cv2.waitKey(0)




