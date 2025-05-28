import turtle


class MyTurtle(turtle.Turtle):
    def __init__(self, shape='turtle', color='black', speed=999):
        super().__init__()
        self.shape(shape)
        self.color(color)
        self.speed(speed)
        self.is_moving = True
        self.target_heading = 0
        self.penup()
        self.move_distance = 4

    def auto_move(self):
        if self.is_moving:
            self.forward(self.move_distance)
            self.screen.ontimer(self.auto_move, 100)

    def turn_up(self):
        self.setheading(90)

    def turn_down(self):
        self.setheading(270)

    def turn_left(self):
        self.setheading(180)

    def turn_right(self):
        self.setheading(0)
