from my_turtle import MyTurtle
from game_screen import GameScreen

# turtle configs
turtle = MyTurtle("turtle")
game_screen = GameScreen(turtle)


# functions

def quit_program(): game_screen.screen.bye()

game_screen.init_turtle_for_draw_key()
game_screen.draw_move_key()
game_screen.init_turtle_for_playing()

# event listener
game_screen.screen.listen()
game_screen.screen.onkey(turtle.move_up, "Up")
game_screen.screen.onkey(turtle.move_down, "Down")
game_screen.screen.onkey(turtle.move_left, "Left")
game_screen.screen.onkey(turtle.move_right, "Right")
game_screen.screen.onkey(game_screen.clear_screen, "c")
game_screen.screen.onkey(quit_program, "q")

game_screen.screen.mainloop()
