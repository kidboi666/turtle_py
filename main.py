from game import Game


# 게임 실행 함수
def main():
    game = Game()
    game.initialize()
    game.start_game()
    game.screen.mainloop()


# 게임 실행 (실제 main.py 가 직접 실행될때만 실행)
if __name__ == "__main__":
    main()
