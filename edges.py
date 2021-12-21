# Uses image convolution to find the edges in an image

import sys
from PIL import Image, ImageFilter

# Check for proper usage and grab the image filename
if len(sys.argv) == 1:
    imfile = input('Name of imagefile: ')
elif len(sys.argv) == 2:
    imfile = sys.argv[1]
else:
    sys.exit("Usage: python3 edges.py imagefile")

with Image.open(imfile) as im:
    # Apply a filter that detects edges
    filtered = im.filter(ImageFilter.CONTOUR)

    filtered.show()
