'''
zero.py zeros the lowest 4 bits in all channels of the input image.  The input
image is changed.  The resulting image is saved.
'''

import sys
from PIL import Image


def zero_lowest_bits(v):
    '''Zero lowest 4 bits of an 8-bit input'''
    return (v & 0b11110000)


def zero_image_lowest_bits(src, dest):
    '''Zeroing lowest 4 bits in all channels of input image'''
    for x in range(src.size[0]):
        for y in range(src.size[1]):
            r, g, b = src.getpixel((x,y))
            new_r = zero_lowest_bits(r)
            new_g = zero_lowest_bits(g)
            new_b = zero_lowest_bits(b)
            dest.putpixel((x,y), (new_r, new_g, new_b))

def main():
    # Check for proper usage and grab the input filename
    if len(sys.argv) == 1:
        imfile = 'images/' + input('Filename of input image: ')
    elif len(sys.argv) == 2:
        imfile = 'images/' + sys.argv[1]
    else:
        sys.exit("Usage: python3 zero.py imagefile")

    with Image.open(imfile) as im:
        # Create a new frame for resulting image
        im_less = Image.new(im.mode, im.size)

        zero_image_lowest_bits(im, im_less)
        im_less.save('images/zeroed.png')

if __name__ == '__main__':
    main()
