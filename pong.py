import turtle

# Can I finish this on my own? YEAH!

window = turtle.Screen()
window.title("Pong by @danzyxr")
window.bgcolor("black")
window.setup(width=1280, height=720)
window.tracer(0)  # Prevents window from updating?

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("gold")
ball.penup()  # penup() means "the pen is lifted from the paper"
ball.goto(0, 0)

paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.color("red")
paddle_1.penup()
paddle_1.goto(-620, 0)  # Why is the left paddle shifted exactly +10 pixels?

paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.color("blue")
paddle_2.penup()
paddle_2.goto(610, 0)

while True:
    window.update()  # Updates the window each time loop iterates
