# constants.py
from enum import Enum


# 게임 관련 상수들
class GameConfig(Enum):
    # 플레이어
    class Turtle:
        COLOR = "lime"
        SHAPE = "turtle"
        SPEED = 0  # 거북이 속도 (최대)

    # 거북이 길이 구현을 위한 투명 거북이
    class Eraser:
        COLOR = "green"
        SHAPE = "circle"
        SIZE = 3  # 투명 거북이의 스탬프 사이즈

    # 화면 및 좌표
    class Screen:
        WIDTH = 420
        HEIGHT = 420
        INSTRUCT_X = -168
        INSTRUCT_Y = 168
        BG_COLOR = "green"

    # 먹이
    class Food:
        COLOR = "red"
        SHAPE = "circle"
        COUNT = 10
        SIZE = 0.5

    # 그 외
    class Gameplay:
        MOVE_DISTANCE = 4
        MOVE_INTERVAL = 20
        COLLISION_DISTANCE = 15
        BOUNDARY = 200
        SAFE_ZONE = 3
        BODY_GROWTH = 10
        INITIAL_BODY_LENGTH = 5

    # 폰트
    class Font:
        class GameOver:
            FONT = ("Arial", 20, "bold")
            COLOR = "red"

        INSTRUCTION = ("Arial", 16, "normal")
