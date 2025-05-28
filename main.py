from my_turtle import MyTurtle
from game_screen import GameScreen

# turtle configs
turtle = MyTurtle("turtle", "lime", 5)
game_screen = GameScreen(turtle)

# functions
game_screen.init_turtle_for_draw_key()
game_screen.draw_move_key()
game_screen.init_turtle_for_playing()
turtle.auto_move()

# event listener
game_screen.screen.listen()
game_screen.screen.onkey(turtle.turn_up, 'Up')
game_screen.screen.onkey(turtle.turn_down, 'Down')
game_screen.screen.onkey(turtle.turn_left, "Left")
game_screen.screen.onkey(turtle.turn_right, "Right")
game_screen.screen.onkey(game_screen.clear_screen, "c")
game_screen.screen.onkey(game_screen.quit_program, "q")

game_screen.screen.mainloop()
