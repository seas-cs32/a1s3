'''
erase32.py EVENTUALLY removes a moving object or individual from an image using
an unspecified number of similar input images.  For each pixel in the shared
frame, it selects the median pixel value from among these input images and
places it in a new, "cleaned" image.

Handout code for CS32 pset 3, part 1.
'''

import sys
from PIL import Image

# Check for proper usage and grab the image filename
if len(sys.argv) == 1:
    imfile = 'images/' + input('Filename of image: ')
elif len(sys.argv) == 2:
    imfile = 'images/' + sys.argv[1]
else:
    sys.exit("Usage: python3 erase32.py imagefile")

with Image.open(imfile) as im:
    # Apply a filter that enhances the red and desaturates blue/green
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            r, g, b = im.getpixel((x,y))
            im.putpixel((x,y), (r, g//50, b//50))

    im.show()