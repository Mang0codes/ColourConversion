import cv2
# 👉 Bring in the cv2 tool (OpenCV) to work with images

# 1. Read the image (as BGR by default)
image = cv2.imread('example.jpg')
# 👉 Load the picture from the computer (by default in BGR colors)

# Safety check
if image is None:
    raise FileNotFoundError("Could not read the image. Check the file path.")
# 👉 If picture not found, show an error and stop the program

# 2. Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# 👉 Change the picture colors from BGR (blue-green-red) to RGB (red-green-blue)

# 3. Convert to Grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 👉 Turn the picture into black and white shades (grayscale)

# 4. Crop the image (rows 100 to 300, columns 200 to 400)
cropped = image[100:300, 200:400]
# 👉 Cut out a smaller part of the picture (like zooming into a box)

# 5. Optional: Display each image (works in standalone scripts/windowed environments)
cv2.imshow('Original (BGR)', image)
# 👉 Show the normal picture (BGR)

cv2.imshow('RGB Version', image_rgb)
# 👉 Show the picture with corrected colors (RGB)

cv2.imshow('Grayscale', image_gray)
# 👉 Show the black and white version

cv2.imshow('Cropped Region', cropped)
# 👉 Show the cut-out (cropped) part of the picture

cv2.waitKey(0)
# 👉 Keep the picture windows open until you press any key

cv2.destroyAllWindows()
# 👉 Close all the picture windows
