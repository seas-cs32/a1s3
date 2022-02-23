This directory contains everything you need as a student for Act I,
Scene III (Numbers).

The following files are used in **Problem #6 (Can you see my dog?)**:

`edges.py, edge[1-4].py`: Scripts we use together in class to understand edge
detection.

`count.py`, `count2.py`: Scripts we use together in class to explore the
limitations of counting with integers.

`images/cosmo.jpg`: Small JPEG of my dog Cosmo.


Additional files used in **Hw #6 (Color the World)**:

`images/duck1.jpg`: Small JPEG of a ddb50 duck.

`color32.py`: Script used to gain familiarity with RGB mode.


Additional files used in **Problem #7 (What is my problem?)**:

`images/photobomb[1-3].jpg`: Three images of Waldo moving through Harvard Yard.
We'd like the picture of the Yard with Waldo removed.  We created this sequence
of pictures by copying a single picture of Harvard Yard and then inserting Waldo
in three different locations.

`zero.py`: Script illustrating the clearing of the lowest 4 bits in each channel
of the pixels in an image.

`images/harvard.png`: The original image of Harvard Yard without Waldo
photobombing it.

`images/[waldo,wenda,odlaw].png`: The *Where's Waldo?* characters we use.

`xverse.py`: A script that uses simple modifications to images to illustrate
different traversals of 2-dimensional data.


Additional files used in **Pset #3 (Erase Waldo, Hide Wenda, Find Wenda, not Odlaw)**:

`pset3.md`: The description of the programming assignment for Act I,
Scene III. Please see the syllabus for when it is due.

`erase_32.py`: The starter code for part 1 of pset 3.  Its code contents
are the same as `color32.py`.

`images/photobomb[1-3].jpg`: Described above.

`images/duck[1-3].jpg`: Three images of a common background and an object (the
CS50 ddb duck) that we'd like to eliminated.  This is a real sequence of three
pictures, and as such, even the pixels where the duck isn't even placed are
subtly different from picture to picture.

`images/apsu[1-6].jpg`: Seven actual images of a common background and a person
who we'd like to remove from the picture.  The unintended subject overlaps
himself in any three of these pictures, and thus we need more than three
pictures to completely remove him.  Thanks again to John Nicholson, from whose
original assignment we got these pictures.

`images/photobomb-mode.jpg`: The result of a version of the `erase32` script
that uses `statistics.mode` instead of `statistics.median`.  It looks good,
right?

`images/duck-mode.jpg`: The result of a version of the `erase32` script that
uses `statistics.mode` instead of `statistics.median`.  It does NOT look good!
Your answer to pset3, part 1, step 4 will explain why.

`pset3_part2.ipynb`: The interactive Python notebook you need to complete part 2
of pset3.  This notebook uses `images/[harvard,waldo,wenda,odlaw].png`.

`images/harvard2.png`: A pre-made Harvard-Yard-with-hidden-Waldo image, in case
you need it for pset3, part 2, step 3.

`pset3_part3.ipynb`: The interactive Python notebook you need to complete part 3
of pset3.


Additional files used in **Short p7-1 (Measurement and Precision)**:

`fbin.py`: Determine the binary encoding for a decimal fraction.
