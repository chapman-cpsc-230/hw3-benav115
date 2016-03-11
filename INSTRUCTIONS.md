# Instructions

This assignment is due on Friday March 11 at 8:00AM. I will start grading on Friday morning. I suggest you plan to submit the work no later than Thursday evening.

## This Assignment

### From the text

From the text, do the following exercises:

* 2.17 -- you submit a file named `booleans.py`. Put your responses in the file as comments following each line.
* 2.18 -- you submit a file named `repeated_sqrt.py`. Put your explanation of results in comments.

### `For`loops

#### Polygons
Write a program that asks the user for two natural numbers `n` and `side_len` and produces a regular `n` sided polygon with each side of length `side_len`. For example, suppose the user responds as follows:

```
Enter number of sides: 5
Enter length of each side: 10
```
Then your program should produce the following picture:


![turtle pentagon](https://github.com/mandrewmoshier/hw3-/blob/master/pentagon.png)

You may use the file *turtlestarter.py* included in this repo as a starter.

Submit a file named *turtlepoly.py*.

#### Stars

Write a program that asks the user for an odd natural number `n` (needs to be at least 5) and a natural number `side_len` and produces an `n`-pointed star with `side_len` length between points. For example, suppose the user responds as follows:

```
Enter number of sides: 11
Enter length of each side: 200
```
Then your program should produce the following picture:


![turtle hendecagram](https://github.com/mandrewmoshier/hw3-/blob/master/hendecagram.png)

You may use the file *turtlestarter.py* included in this repo as a starter.

Submit a file named *turtlestar.py*.

Hint: To get the turtle to turn correctly at each point of the star, think about how many total rotations the turtle will need to make to complete the figure. For a pentagram, it will be two full rotations (720 degrees). For a heptagram (a seven pointed star) it will be three full rotations (1080 degrees).

*Bonus:* Can you figure out how to reposition the turtle before drawing so the star is centered left-to-right in its window? Assuming your turtle is named `t` you can

* Lift the pen from the page by the command `t.up()`
* Put the pen back down by the command `t.down()`

## General


* Edit the README.md file:
    * Change _\<your name\>_ and _\<date\>_ at the beginning of the file
    * Reread the __Honor Pledge__ again and 'sign' it with your name at the end
    * Add your own text in the __Description__ and __What I Learned__ sections

* Correctly document each source file
    * At the top of each source file (```.py``` file), include a docstring in te following format

    ```
    """
    File: <filename>

    Copyright (c) 2016 <your name>

    License: MIT

    <brief description of the code>
    """    
    ```
