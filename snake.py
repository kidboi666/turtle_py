# snake.py
import turtle

from constants import GameConfig


# 스네이크 로직 클래스
class Snake(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape(GameConfig.Turtle.SHAPE)
        self.color(GameConfig.Turtle.COLOR)
        self.speed(GameConfig.Turtle.SPEED)

        self.is_moving = True
        self.path_positions = []
        self.body_length = GameConfig.Gameplay.INITIAL_BODY_LENGTH
        self.move_distance = GameConfig.Gameplay.MOVE_DISTANCE

        self._setup_eraser()
        self._reset_position()

    # 상태 초기화
    def reset_state(self):
        self.clear()
        self.eraser.clear()
        self.path_positions = []
        self.body_length = GameConfig.Gameplay.INITIAL_BODY_LENGTH
        self.is_moving = True
        self.setheading(0)
        self.color(GameConfig.Turtle.COLOR)
        self.showturtle()
        self._reset_position()

    # 앞으로 이동
    def move_forward(self):
        if not self.is_moving:
            return

        self.forward(self.move_distance)
        current_position = (round(self.xcor()), round(self.ycor()))

        if not self.path_positions or self.path_positions[-1] != current_position:
            self.path_positions.append(current_position)

        if len(self.path_positions) > self.body_length:
            old_position = self.path_positions.pop(0)
            self.eraser.goto(old_position)
            self.eraser.stamp()

    # 몸통 길이 늘리기
    def grow_body(self):
        self.body_length += GameConfig.Gameplay.BODY_GROWTH

    # 위로
    def turn_up(self):
        if self.heading() != 270:
            self.setheading(90)

    # 아래로
    def turn_down(self):
        if self.heading() != 90:
            self.setheading(270)

    # 왼쪽 으로
    def turn_left(self):
        if self.heading() != 0:
            self.setheading(180)

    # 오른쪽 으로
    def turn_right(self):
        if self.heading() != 180:
            self.setheading(0)

    # 멈추기
    def stop_moving(self):
        self.is_moving = False

    # 자살 여부 판독
    def check_self_collision(self):
        current_pos = (round(self.xcor()), round(self.ycor()))
        safe_zone = GameConfig.Gameplay.SAFE_ZONE

        if len(self.path_positions) > safe_zone:
            return current_pos in self.path_positions[:-safe_zone]
        return False

    # 화면 외부 영역 감지
    def is_out_of_bounds(self):
        boundary = GameConfig.Gameplay.BOUNDARY
        return abs(self.xcor()) > boundary or abs(self.ycor()) > boundary

    # 스네이크 위치 재설정
    def _reset_position(self):
        self.penup()
        self.goto(0, 0)
        self.pendown()

    # 투명 거북이 초기화
    def _setup_eraser(self):
        self.eraser = turtle.Turtle()
        self.eraser.shape(GameConfig.Eraser.SHAPE)
        self.eraser.color(GameConfig.Eraser.COLOR)
        self.eraser.speed(0)
        self.eraser.hideturtle()
        self.eraser.penup()
