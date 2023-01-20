import sounddevice as sd
import numpy as np
import pygame



# Initializes all pygame modules
pygame.init()
# Sets the FPS to 60
FPS = 60
# Creates a window with size 900 x 600
WIN = pygame.display.set_mode((1600, 900))
# Sets the caption of the game
pygame.display.set_caption("My game")


# The function that draws everything in the pygame window
# Everything will be drawn on top of each other
# If you want to reset the window you can do .fill with your choice of rgb tuple as parameter
# Always update the window in the end of the draw function
def draw(indata, outdata, frames, time, status):
    color = (255,255,255) if int(np.linalg.norm(indata) * 10) <10 else (255,0,0)
    WIN.fill(color)

    pygame.display.update()


def main():
    # Creates a clock so it can tick with the given FPS
    clock = pygame.time.Clock()
    clock.tick()
    # Sets game_over to False so the while loop can run as long as it is not game over

    with sd.Stream(callback=draw):
        sd.sleep(10000)


if __name__ == "__main__":
    main()
