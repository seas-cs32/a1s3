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
        pixels[i,j] = 0 if i < 25 else 255    # vertical boundary
        # pixels[i,j] = 0 if j < 25 else 255    # horizontal boundary

# Show initial image
im.show()

# Create a new B&W image into which we'll put the filtered result
filtered = Image.new('L', sz)
fpixels = filtered.load()

# Apply an edge-detection convolution (it's just math for B&W only!)
for i in range(1, sz[0]-1):
    for j in range(1, sz[1]-1):
        fpixels[i,j] = (pixels[i-1,j-1] * -1 + pixels[i-1,j] * -1 + pixels[i-1,j+1] * -1 +
                        pixels[i  ,j-1] * -1 + pixels[i  ,j] * 8  + pixels[i  ,j+1] * -1 + 
                        pixels[i+1,j-1] * -1 + pixels[i+1,j] * -1 + pixels[i+1,j+1] * -1)

# Show resulting image
filtered.show()
