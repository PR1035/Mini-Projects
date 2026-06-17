from PIL import Image
from colorama import Fore, Style

img = Image.open("pineapple.jpg", mode="r")

width, height = img.size


#Getting 2D array of pixels
rgb_array = []

def get_rgb_array():
    """ img.thumbnail((height, 200))
    for y in range(height):
        row = []
        for x in range(width):
            row.append(img.getpixel((x, y)))
        rgb_array.append(row)
    return rgb_array """
    img.thumbnail((height, 200))
    pixels = list(img.getdata())
    return [pixels[i:i+img.width] for i in range(0, len(pixels), img.width)]
# print(rgb_array)
get_rgb_array()

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
# print(img.size)
# print(brightness_array)
