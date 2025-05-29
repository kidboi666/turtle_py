import turtle
from constants import bg_color

class GameScreen:
    def __init__(self, t, width = 600, height = 600, startx=1100, starty=200, bg_color = bg_color):
        self.t = t
        self.screen = turtle.Screen()
        self.screen.setup(width, height, startx, starty)
        self.screen.bgcolor(bg_color)
        self.current_heading = self.t.heading()

    def clear_screen(self):
        self.screen.clear()

    def move_next_line(self):
        self.t.penup()
        self.t.rt(90)
        self.t.fd(20)
        self.t.pendown()
        self.t.setheading(self.current_heading)

    def init_screen(self):
        self.t.penup()
        self.t.goto(-280, 280)
        self.t.write("move to forward : ↑", font=("Arial", 20, "normal"))
        self.move_next_line()
        self.t.write("move to back : ↓", font=("Arial", 20, "normal"))
        self.move_next_line()
        self.t.write("move to left : ←", font=("Arial", 20, "normal"))
        self.move_next_line()
        self.t.write("move to right : →", font=("Arial", 20, "normal"))
        self.t.penup()
        self.t.goto(0, 0)
        self.t.pendown()

    def quit_program(self):
        self.screen.bye()

    def reset_game(self):
        self.t.reset_game()
        self.init_screen()
        self.t.auto_move()

