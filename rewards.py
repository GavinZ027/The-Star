import turtle

# Create a turtle object
star = turtle.Turtle()

# Set the fill color to yellow
star.fillcolor('yellow')

# Start filling the star
star.begin_fill()

# Draw the star
for i in range(5):
    star.forward(100)
    star.right(144)

# End filling the star
star.end_fill()

# Hide the turtle object
star.hideturtle()

# Display the window
turtle.done()
