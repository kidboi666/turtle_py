import turtle
from constants import turtle_color

class MyTurtle(turtle.Turtle):
    def __init__(self, shape, color, speed):
        super().__init__()
        self.shape(shape)
        self.color(color)
        self.speed(speed)
        self.is_moving = True
        self.game_over = False
        self.target_heading = 0
        self.path_positions = []
        self.penup()
        self.move_distance = 1

    def reset_game(self):
        self.clear()
        self.penup()
        self.goto(0, 0)
        self.pendown()
        self.path_positions = []
        self.game_over = False
        self.setheading(0)
        self.color(turtle_color)

    def start_game(self):
        self.auto_move()

    def auto_move(self):
        if self.is_moving and not self.game_over:
            current_position = (round(self.xcor()), round(self.ycor()))

            if current_position in self.path_positions:
                self.game_over = True
                self.color('red')
                self.write("GAME OVER", font=("Arial", 20, "normal"))
                return

            if self.is_out_of_bounds():
                self.game_over = True
                self.color('red')
                self.write("GAME OVER", font=("Arial", 20, "normal"))
                return

            self.path_positions.append(current_position)
            self.forward(self.move_distance)
            self.screen.ontimer(self.auto_move, 4)

    def is_out_of_bounds(self):
        x, y = self.xcor(), self.ycor()
        return x < -290 or x > 290 or y < -290 or y > 290

    def turn_up(self):
        if not self.game_over:
            self.setheading(90)

    def turn_down(self):
        if not self.game_over:
            self.setheading(270)

    def turn_left(self):
        if not self.game_over:
            self.setheading(180)

    def turn_right(self):
        if not self.game_over:
            self.setheading(0)
