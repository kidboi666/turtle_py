# game.py
import turtle

from constants import GameConfig
from food import Food
from snake import Snake


# 게임 동작 로직이 정의된 클래스
class Game:
    def __init__(self):
        self.snake = Snake()
        self.foods = []
        self.score = 0
        self.game_over = False
        self._setup_screen()
        self._setup_controls()

    # 초기 화면 설정
    def _setup_screen(self):
        self.screen = turtle.Screen()
        config = GameConfig.Screen
        self.screen.setup(
            config.WIDTH,
            config.HEIGHT,
        )
        self.screen.bgcolor(config.BG_COLOR)
        self.screen.listen()

    # 조작키 바인딩
    def _setup_controls(self):
        self.screen.onkey(self.snake.turn_up, "Up")
        self.screen.onkey(self.snake.turn_down, "Down")
        self.screen.onkey(self.snake.turn_left, "Left")
        self.screen.onkey(self.snake.turn_right, "Right")
        self.screen.onkey(self.reset_game, "r")
        self.screen.onkey(self.screen.bye, "q")

    # 먹이 초기화
    def _clear_foods(self):
        for food in self.foods:
            food.hideturtle()
        self.foods.clear()

    # 먹이 초기화 실행 이후 랜덤 좌표를 가진 먹이 출력
    def _spawn_foods(self):
        self._clear_foods()
        for _ in range(GameConfig.Food.COUNT):
            food = Food()
            food.spawn_random_position()
            self.foods.append(food)

    # 화면 좌상단 텍스트 출력
    def _show_instructions(self):
        self.snake.penup()
        self.snake.goto(GameConfig.Screen.INSTRUCT_X, GameConfig.Screen.INSTRUCT_Y)
        instructions = [
            "move to forward : ↑",
            "move to back : ↓",
            "move to left : ←",
            "move to right : →",
            "Press 'r' to restart, 'q' to quit",
        ]

        for instruction in instructions:
            self.snake.write(instruction, font=GameConfig.Font.INSTRUCTION)
            self.snake.right(90)
            self.snake.forward(20)
            self.snake.left(90)

        self.snake.goto(0, 0)
        self.snake.pendown()

    # 먹이 습득시 로직
    def _check_food_collision(self):
        snake_pos = (round(self.snake.xcor()), round(self.snake.ycor()))

        for food in self.foods:
            food_pos = (round(food.xcor()), round(food.ycor()))
            distance = (
                (snake_pos[0] - food_pos[0]) ** 2 + (snake_pos[1] - food_pos[1]) ** 2
            ) ** 0.5

            if distance < GameConfig.Gameplay.COLLISION_DISTANCE:
                food.spawn_random_position()
                self.snake.grow_body()
                self.score += 1
                return True
        return False

    # 게임 오버 여부, 먹이 습득 여부를 반복 실행해 게임 상태 검증
    def _game_loop(self):
        if self.game_over:
            return

        if self.snake.is_out_of_bounds() or self.snake.check_self_collision():
            self._handle_game_over()
            return

        self.snake.move_forward()
        self._check_food_collision()
        self.screen.ontimer(self._game_loop, GameConfig.Gameplay.MOVE_INTERVAL)

    # 게임 오버
    def _handle_game_over(self):
        self.game_over = True
        self.snake.stop_moving()
        self.snake.penup()
        self.snake.goto(0, 0)
        self.snake.color(GameConfig.Font.GameOver.COLOR)
        self.snake.write(
            f"GAME OVER\nScore: {self.score}\nPress 'r' to restart",
            align="center",
            font=GameConfig.Font.GameOver.FONT,
        )

    # 메인 로직 실행
    def start_game(self):
        self.game_over = False
        self.snake.is_moving = True
        self._spawn_foods()
        self._game_loop()

    # 게임 리셋
    def reset_game(self):
        self.score = 0
        self.game_over = False
        self._clear_foods()
        self.screen.clear()
        self.screen.bgcolor(GameConfig.Screen.BG_COLOR)
        self.snake = Snake()
        self._setup_controls()
        self._show_instructions()
        self.start_game()

    # 화면 도움말 출력
    def initialize(self):
        self._show_instructions()
