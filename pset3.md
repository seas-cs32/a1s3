## CS32 Act I, Scene III -- Programming Assignment

*NOTE: The ["PSet3" assignment page on the CS 32 Canvas
site](https://canvas.harvard.edu/courses/97999/assignments/535596) indicates
when this assignment is due, what materials you should submit, and how to submit
them.*

### ### Big Picture

This assignment has three parts through which you will have the opportunity to
act a bit like a data scientist.  You'll recall that data scientists begin their
work by collecting some data and then cleaning it so that they can explore it
looking for interesting patterns.  If they find something interesting, they'll
build a computational model with which they can make predictions or assist in
decision-making.  As mentioned in class, this assignment focuses on data
cleaning (parts 1 and 2) and data exploration (part 3).  It builds off our
knowledge of digital images and has fun with the wacky world of Where's Waldo?


### ### Assignment, Part 1: Erase Waldo

We learned in class that digital images are nothing more than large
two-dimensional arrays of numbers, which we can load into a pixel array and
manipulate.  The first part of this assignment allows you to put this new
knowledge to work by solving a common problem: removing an unintended subject in
a sequence of pictures containing no moving objects except for our unintended
subject.[^1]

This is a simple example of a filter tool.  You can build different types of
filters to remove different kinds of noise found in your digital image files.
For this problem set, we will consider the unintended subject to be the noise
that we want removed automatically by our script.

How will our script remove this noise?  As we discussed in class, it will expect
you to give it *N* pictures, for *N* greater than 2, that are all of the same
size and orientation.  Your script will then visit each pixel location in this
common image frame, read the pixel values at this location for each of the input
pictures, and compute a single output pixel for this location for the final
filtered image.  Our script will determine this outputted pixel by computing a
*median* of the input pixels.

This filtering process will succeed if the picture we want to capture is filled
with stationary objects (e.g., like a landscape or still life), and the
unintended subject is quickly moving around the frame of our picture as we took
the images.  The number of input pictures needed for our approach to be
successful depends upon how often the unintended subject obscured each image
pixel, since we want the majority of the input pixel values to correspond to the
things that the unintended subject only momentarily obscured.

To get us started, we will begin with the script from Hw #6.  It has been
renamed `erase32.py`, but its code contents are the same as you saw in this
previous homework assignment.

**Step 1. Reading multiple input files.**  Change the script `erase32.py` so
that it reads *exactly* three input files from the command line or from user
input.

Then edit the `with Image.open` line so that it opens multiple image objects at
the same time.  The syntax you'll need simply repeats the `as` phrase separated
by commas.

This `with` line might get quite long.  You can split it across multiple lines
using the line continuation character in Python, which is the backslash (`\`).
Take a look at [the Style Guide for Python Code (PEP 8) under "Maximum Line
Length"](https://www.python.org/dev/peps/pep-0008/#maximum-line-length) to see
an example of how this is done.  As it says there, we prefer to use Python's
implied line continuation in most long-line situations rather than this explicit
line continuation syntax, but this is a common situation where you can't use
anything but the explicit syntax.

Finally, add some statements to your script so that it prompts the user to ask
which input file the script should display.  Don't worry about checking for all
kinds of bad input; we'll delete this part of the code in a moment.  Do,
however, make sure that the correct file was displayed when you gave it a good
input value!

To test your script, you can use the image files with the prefix name `duck` or
`photobomb` in the `a1s3/images` directory.

**Step 2. Finding the statistical median.**  Alright, you are now ready to erase
an unintended subject.

First, get rid of the user prompt we included to test our ability to read in
three image files.  You can leave those that prompted the user for the image
filenames.

Next, think about the looping logic you need to adjust the pixel values for each
point in the input images.  Sketch out that logic in pseudo code.  HINT: You
seen it many times to this point.

Now let's think about what takes place in the body of this looping logic.
Although we could write a function that computed a median given a list of
numbers, let's take advantage of the `statistics` library in Python, which has
conveniently provided us with a `statistics.median` function.  You may want to
[read about
it](https://docs.python.org/3/library/statistics.html#statistics.median) before
attempting to complete this step.

You'll notice that the `statistics.median` function may produce a value that is
not one of the input data points.  This will be a problem for us because we
don't want out input integer values turned into an output floating point value.
Our color values are integers and need to stay as integers!  While you might
force the value returned from `statistics.median` back into an integer, we can
also simply use `statistics.median_low`.  Ahh, what a helpful and a
well-designed library!

You are ready to write the Python code that erases the unintended subject.  Do
it!

In testing your code, you might start with the three `photobomb` images in the
`images` directory.  If that works, check your code with the three `duck`
images.  Take a look at the `README.md` file to understand the difference
between the two sets of images.

**Step 3. Adding robustness.**  Congratulations on erasing Waldo from our pretty
picture of Harvard Yard!  As wonderful as our little script is, it isn't very
robust.  For example, it expects exactly three input images, and the unintended
object can't overlap with itself in any of the three images.

To see this second point for yourself, run your solution to step 2 with the
first three images with the prefix `apsu`.  These files have the extension
`.png`.  Look at the resulting image very closely, and you'll see a shadowy
image of the person's feet where the unintended subject overlapped with his
previous self. 

We could eliminate this problem and build a more robust script if we allowed
more input images. The unintended object or subject could then overlap with
itself/himself in some of the input images as long as the majority of the images
contained only the desired background.

Let's finish this part of the assignment by building a script that takes an
unspecified number of input files on the command line, and let's write out the
final result so that we can keep the cleaned-up picture.  You can eliminate, in
this step, the statements that allowed the user to input the image files.
Taking an unlimited number of input files sounds hard, but we'll get through it
together.

First, fix the "proper usage" check so that it expects *at least 3 command line
arguments*.  Remember that the your program's name (but not the `python3`
interpreter) counts as one of the command line arguments.

Next, we need to think about a data structure to keep track of our image objects
that we will open from the input image files.  Previously, we wrote an explicit
set of three `Image.open` commands because we knew that there were exactly three
input files (and thus we could hardcode three image object variables into our
script).  How are we going to rethink this part since we don't know the number
of input image files until the program runs?  Can you think of a data structure
that will allow us to work with a variable-length list of objects?  Yes, we just
said it!  A Python `list` will do this quite nicely.  We'll talk a lot more
about different types of common data structures in the next act.

We are now ready to open image objects for each of our input image files and
keep track of these image objects in a list.  Don't forget that we can ask for
the size of the `sys.argv` list and subtract 1 from this value to determine the
number of input files.  This might be very useful in creating a bound on a loop
that creates the list and later loops that walk over the elements in this list.

This variability in the number of image objects also means that we cannot use
the nice `with` syntax.  We are going to have to open each input image file and
later explicitly close each one (using `Image.close`).  Put those two pieces of
code into your script.  You might go back to our discussion from Scene I about
what `with` does for us if you don't understand this paragraph.

Finally, think about what has to change in your nested loops that walk over each
pixel in the input images.  We're giving you fewer hints here, but you have all
the knowledge you need at this point.

Once you've done this, run your script as follows:

```
python3 erase32.py apsu1.png apsu2.png apsu3.png apsu4.png apsu5.png apsu6.png
```

Did this produce a much cleaner resulting image?  It should!

Oh, you have a wonderful script that should also save your resulting image.  Don't
you want to impress your friends and family?  Add a `save` method call off the
image you `show`-ed.  You might save it as a PNG file in `images/out.png`, but the
choice is really yours.

**Step 4. Why median, but not mode?**  Take a look at the files
`images/photobomb-mode.jpg` and `images/duck-mode.jpg`.  These files were
produced by our solution script to Step 2 above, except that we used
`statistics.mode` instead of `statistics.median` to compute the pixel we placed
in the output image.  As you'll see by looking at these two images, we
successfully erased Waldo using the `mode` function, but not the duck.  Why is
this?  HINT: What's different in how we gathered the original data (i.e.,
images) in these two cases?  And when you figure out why median is more robust
an approach than mode, please explain why is it the first duck that remains.
HINT: This doesn't have anything to do with the statistical properties of the
function, but choices that the library designer made.  What are you learning
about quantitative reasoning with data here?


### ### Assignment, Part 2: Hide Wenda

For the second and third parts of this assignment, we're going to practice
working with Python in an online environment that is meant to look like a
scientist's notebook.  In particular, we will use [Google
Colab](https://colab.research.google.com/notebooks/intro.ipynb), which is the
same environment in which you have been reading the course's draft textbook. The
other popular alternative to Google Colab is [the Jupyter
Notebook](https://jupyter.org/)).  Both are sophisticated web applications in
which you stitch together narrative text with code, images, and other data
visualizations.  Both platforms manipulate files in IPYNB format.

The overarching goal of the code that you'll write for part 2 is to hide an
image of Wenda in our image of Harvard Yard and, of course, later recover that
image.  In doing this work, you'll practice using bitwise operators and get more
comfortable creating code that does limited traversals of the pixels in one or
more images.

Ready to get started?  Great!  Please open `pset3-part2.ipynb` and complete the
work described in it.

Don't forget to execute each code block as you come across it!


### ### Assignment, Part 3: Find Wenda, not Odlaw

For the third and final part of this assignment, we're going to practice writing
code that lets us explore a data set like a data scientist.  In particular,
we'll write Python code that helps us to practice different traversals over the
pixels of an image, and like part 2, we'll do all this work in an interactive
Python notebook.

While you'll write traversals specific to images, the looping structures you'll
build and the thinking you'll do about how to use Python exceptions to cleanly
unwind a computation (i.e., to stop one analysis and start another) will be
useful in the exploration of any kind of data set.

Ready to finish this pset?  Alright!  Please open `pset3-part3.ipynb` and
complete the work described in it.

Don't forget to execute each code block as you come across it!


### ### Optional, Fun, Current-Event Reading

*FIXME: Any?*


### Footnotes

[^1]: This problem was inspired by John Nicholson's 2014 [Nifty
Assignment](http://nifty.stanford.edu) titled [The Pesky
Tourist](http://nifty.stanford.edu/2014/nicholson-the-pesky-tourist/).  We thank
him for sharing it with the world.