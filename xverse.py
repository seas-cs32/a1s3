'''
xverse.py -- uses an image to illustrate different traversals

By default, it runs a row-major traversal and inverts the pixels it
touches along the way.  In short, it's a traverse-inverse (aka xverse).

It stores the modified image in images/xverse.png
'''

import sys
from PIL import Image


# Many fun do_something functions the students might try
def grayscale(pixel):
    '''Turn pixel into grayscale'''
    r, g, b = pixel
    gray = (r + g + b) // 3
    return (gray, gray, gray)

def sepia(pixel):
    '''Give the pixel a sepia tone'''
    r, g, b = pixel
    tr = int(0.393 * r + 0.769 * g + 0.189 * b)
    r = 255 if tr > 255 else tr
    tg = int(0.349 * r + 0.686 * g + 0.168 * b)
    g = 255 if tg > 255 else tg
    tb = int(0.272 * r + 0.534 * g + 0.131 * b)
    b = 255 if tb > 255 else tb
    return (r, g, b)

def inverse(pixel):
    '''Reverse video the input pixel'''
    r, g, b = pixel
    return (256 - r, 256 - g, 256 - b)


def traverse(im, x, y):
    '''Traverse an image from (0,0) until location (x,y)
       and do something at each visited pixel.  The input
       image is unchanged, and the changed image is returned.
    '''
    # Create an image frame and initialize it with the input image
    new_im = im.copy()

    for i in range(im.size[0]):
        for j in range(im.size[1]):
            pixel = im.getpixel((i,j))
            new_im.putpixel((i,j), inverse(pixel))
            
            if (i == x and j == y):
                return new_im


def main():
    # Check for proper usage and grab input
    if len(sys.argv) == 1:
        imfile = 'images/' + input('Filename of input image: ')
        pt = input('Where should we stop? ')
        xy = [int(d) for d in pt.split(',')]
    elif len(sys.argv) == 4:
        imfile = 'images/' + sys.argv[1]
        xy = [int(sys.argv[2]), int(sys.argv[3])]
    else:
        sys.exit("Usage: python3 xverse.py image x y")

    with Image.open(imfile) as im:
        # Verify that x,y is within the input image
        assert(xy[0] < im.size[0] and xy[1] < im.size[1])

        new_im = traverse(im, xy[0], xy[1])
        new_im.save('images/xverse.png')

if __name__ == '__main__':
    main()
