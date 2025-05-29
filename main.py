from my_turtle import MyTurtle
from game_screen import GameScreen
from constants import turtle_color, turtle_shape, turtle_speed


turtle = MyTurtle(turtle_shape, turtle_color, turtle_speed)
game_screen = GameScreen(turtle)

game_screen.init_screen()
turtle.auto_move()

game_screen.screen.listen()
game_screen.screen.onkey(turtle.turn_up, 'Up')
game_screen.screen.onkey(turtle.turn_down, 'Down')
game_screen.screen.onkey(turtle.turn_left, "Left")
game_screen.screen.onkey(turtle.turn_right, "Right")
game_screen.screen.onkey(game_screen.reset_game, "r")
game_screen.screen.onkey(game_screen.quit_program, "q")

game_screen.screen.mainloop()
