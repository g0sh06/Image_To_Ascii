import cv2
import json

# defining the array with ASCII character
ascii_chars = ['@', '%', '#', '*', '+', '=', '-', ':', '.', '?', '>', '<', '|', '}', '{']

#open the image
img = cv2.imread('picture.jpg')
heigth, width = img.shape[0], img.shape[1]

#resizing the image
aspect_ratio = heigth / width
new_width = 100
new_height = int(new_width * aspect_ratio)
resized_image = cv2.resize(img, (new_width, new_height))
pixel_value = []

#transforming the picture into gray colors
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

#getting the color pallete of every pixel
for y in range(heigth):
    for x in range(width):
        pixel_value.append((x, y))

ascii_art = ''

#transforming the different gray patterns into different ASCII characters
for row in gray_image:
    for pixel_value in row:
        ascii_index = int(pixel_value / 255 * len(ascii_chars) - 1)
        ascii_art += ascii_chars[ascii_index]
    ascii_art += '\n'

#displaying the good job
print(ascii_art)
cv2.imshow('Original image', img)
cv2.imshow('Modified image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

