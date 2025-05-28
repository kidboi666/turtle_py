import turtle

class MyTurtle(turtle.Turtle):
    def __init__(self, shape='turtle', color='black',speed=5):
        super().__init__()
        self.shape(shape)
        self.color(color)
        self.speed(speed)
        self.penup()
        self.move_distance = 20

    def move_up(self):
        y = self.ycor()
        self.goto(self.xcor(), y + self.move_distance)

    def move_down(self):
        y = self.ycor()
        self.goto(self.xcor(), y - self.move_distance)

    def move_left(self):
        x = self.xcor()
        self.goto(x - self.move_distance, self.ycor())

    def move_right(self):
        x = self.xcor()
        self.goto(x + self.move_distance, self.ycor())
