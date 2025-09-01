import cv2
import numpy as np
# 👉 Bring in special tools: cv2 for images, numpy (np) for math with images

# 1. Read the image
image = cv2.imread('example.jpg')
# 👉 Load the picture from the computer into Python

# Safety check
if image is None:
    raise FileNotFoundError("Could not read the image. Check the file path.")
# 👉 If picture not found, show an error

# ------------------------------
# Rotate the image by 45 degrees
# ------------------------------

# Get the image dimensions
(h, w) = image.shape[:2]  
# 👉 Find how tall (h) and wide (w) the picture is

# Find the center of the image
center = (w // 2, h // 2)
# 👉 Find the middle point of the picture

# Get rotation matrix: rotate by 45° around the center, scale = 1.0
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
# 👉 Make a formula that tells the computer how to turn the picture

# Perform the rotation
rotated = cv2.warpAffine(image, rotation_matrix, (w, h))
# 👉 Actually spin the picture by 45 degrees

# ------------------------------
# Increase brightness
# ------------------------------

# Make a matrix of ones same size as image, multiplied by 50
brightness_matrix = np.ones(image.shape, dtype="uint8") * 50
# 👉 Create a bright sheet (50 brighter) same size as the picture

# Add brightness safely (avoids overflow above 255)
brighter = cv2.add(image, brightness_matrix)
# 👉 Add the bright sheet to the picture to make it lighter

# ------------------------------
# Show results
# ------------------------------
cv2.imshow("Original", image)
# 👉 Show the normal picture

cv2.imshow("Rotated by 45 degrees", rotated)
# 👉 Show the picture turned 45 degrees

cv2.imshow("Brighter Image", brighter)
# 👉 Show the brighter picture

cv2.waitKey(0)
# 👉 Wait until you press any key to close the pictures

cv2.destroyAllWindows()
# 👉 Close all the picture windows
