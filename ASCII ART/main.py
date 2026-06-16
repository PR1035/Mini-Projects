from PIL import Image
from colorama import Fore, style

img = Image.open("pineapple.jpg", mode="r")

width, height = img.size

#Getting 2D array of pixels
rgb_array = []
for y in range(height):
    row = []
    for x in range(width):
        row.append(img.getpixel((x, y)))
    rgb_array.append(row)
# print(rgb_array)

brightness_array = []
for i in rgb_array:
    brightness_row = []
    for j in i:
        avg = (j[0] + j[1] + j[2])/3.0
        brightness_row.append(avg)
    brightness_array.append(brightness_row)
""" 
    `^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$
 """

s = '`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'

char_array = []
for i in brightness_array:
    char_row = []
    for j in i:
        variable = int(((j/255.0) * 66) - 1)
        chara = s[variable]
        char_row.append(chara)
    char_array.append(char_row)

for i in char_array:
    print(i*3)

# img.show()
print(img.size)
# print(brightness_array)
