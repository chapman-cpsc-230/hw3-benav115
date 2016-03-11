
import turtle

# Ask user for input here.
num_sides_inp = raw_input("Enter an odd number larger than 5: ")
num_sides = int(num_sides_inp)
side_len_inp = raw_input("Enter a length: ")
side_len = int(side_len_inp)
# Now create a graphics window.
t = turtle.Pen()

# Put the rest of your code can go here
for side in range(num_sides):
    t.forward(side_len)
    t.left(180-180/num_sides)
# Prevent the graphics window from diappearing too
# quickly to see it.
stopper = raw_input("Hit <enter> to quit.")

# Now remove the graphics window before exiting.
turtle.bye()
