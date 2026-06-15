from PIL import Image

img = Image.open("pineapple.jpg", mode="r")

width, height = img.size

#Getting 2D array of pixels
rgb_array = []
for y in range(height):
    row = []
    for x in range(width):
        row.append(img.getpixel((x, y)))
    rgb_array.append(row)
print(rgb_array)


img.show()
print(img.size)
