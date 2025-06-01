# food.py
import random
import turtle

from constants import GameConfig


# 먹이 로직 클래스
class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape(GameConfig.Food.SHAPE)
        self.color(GameConfig.Food.COLOR)
        self.penup()
        self.shapesize(GameConfig.Food.SIZE, GameConfig.Food.SIZE)
        self.speed(0)

    # 화면 내부에서
    def spawn_random_position(self):
        boundary = GameConfig.Gameplay.BOUNDARY - 20
        x = random.randint(-boundary, boundary)
        y = random.randint(-boundary, boundary)
        self.goto(x, y)
