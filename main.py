from pprint import pformat
from statistics import median_grouped

import pygame
import sys
from config import *
from game import Game

def main():
    try:
        # inicializar juego
        pygame.init()
        game =Game()
        game.run()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
    finally:
        pygame.quit()
        sys.exit()
if __name__ == "__main__":
    main()