import turtle

bob = turtle.Turtle()
bob.speed(0)


def draw_square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


draw_square(bob, 100)
draw_square(bob, 50)


def draw_polygon(t, length, n):
    theta = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(theta)


draw_polygon(bob, 100, 9)

turtle.mainloop()
