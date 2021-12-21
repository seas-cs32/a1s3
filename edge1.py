# Build a simple image containing an obvious edge

from PIL import Image

# Width and height of our image
sz = (100, 100)

# Create a single plane of black and white pixels, initialized to black
im = Image.new('L', sz)

# Create direct access to the pixels in the image
pixels = im.load()

# Set the color of each pixel
for i in range(sz[0]):
    for j in range(sz[1]):
        # Creates a diagonal fade
        pixels[i,j] = i + j

im.show()
