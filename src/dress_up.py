import pygame

def main():
    pygame.init()

    # Create window
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Tuppence Dress Up")

    # Controls how fast the game runs
    clock = pygame.time.Clock()

    # Game loop
    running = True

    while running:

        # Check events
        for event in pygame.event.get():

            # If player closes window
            if event.type == pygame.QUIT:
                running = False

        # Fill background color
        screen.fill((255, 200, 200))

        # Update screen
        pygame.display.update()

        # 60 frames per second
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()