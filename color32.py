'''
color32.py desaturates blue, green to highlight red and demonstrate
RGB nature of 3-color channels for each pixel (8-bit, 8-bit, 8-bit)

Handout code for CS32 homework #6.
'''

import sys
from PIL import Image

# Check for proper usage and grab the image filename
if len(sys.argv) == 1:
    imfile = 'images/' + input('Filename of image: ')
elif len(sys.argv) == 2:
    imfile = 'images/' + sys.argv[1]
else:
    sys.exit("Usage: python3 color32.py imagefile")

with Image.open(imfile) as im:
    # Apply a filter that enhances the red and desaturates blue/green
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            r, g, b = im.getpixel((x,y))
            im.putpixel((x,y), (r, g//50, b//50))

    im.show()