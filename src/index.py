from tkinter import Tk
from game import Game
from ui.game_ui import GameView


def main():
    display = Tk()
    game = Game()

    game_ui = GameView(display, game)
    game_ui.start()

    display.mainloop()

if __name__ == '__main__':
    main()