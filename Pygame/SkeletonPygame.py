import sys, pygame

# Initializes all pygame modules
pygame.init()
#Sets the FPS to 60
FPS = 60
# Creates a window with size 900 x 600
WIN = pygame.display.set_mode((900, 600))
# Sets the caption of the game
pygame.display.set_caption("My game")

# The function that draws everything in the pygame window
# Everything will be drawn on top of each other
# If you want to reset the window you can do .fill with your choice of rgb tuple as parameter
# Always update the window in the end of the draw function
def draw(window):
    WIN.fill((255,125,125))

    pygame.display.update()



def main():
    # Creates a clock so it can tick with the given FPS
    clock = pygame.time.Clock()
    # Sets game_over to False so the while loop can run as long as it is not game over
    game_over = False


    while not game_over:
        # The tick method makes sure the while loop only do 60 iterations per second if FPS = 60
        clock.tick(FPS)
        # This is the key for pygame. A lot of different actions gets saved in a list
        # You loop through this list and do different things based on those actions
        # An action can be a mouseclick, buttonclick etc.
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        # Last in the while loop we call the draw function to update the window
        draw(WIN)


if __name__ == "__main__":
    main()
