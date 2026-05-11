import pygame


# LOAD IMAGES
def load_images():

    body = pygame.image.load("images/body.png").convert_alpha()

    shirt1 = pygame.image.load("images/shirt1.png").convert_alpha()

    return body, shirt1


# HANDLE EVENTS
def handle_events(shirt_button, shirt1, current_shirt):

    running = True

    for event in pygame.event.get():

        # CLOSE WINDOW
        if event.type == pygame.QUIT:
            running = False

        # MOUSE CLICK
        if event.type == pygame.MOUSEBUTTONDOWN:

            if shirt_button.collidepoint(event.pos):

                current_shirt = shirt1

    return running, current_shirt


# DRAW EVERYTHING
def draw_game(screen, body, current_shirt, shirt_button):

    # BACKGROUND
    screen.fill((255, 200, 200))

    # BODY
    screen.blit(body, (250, 100))

    # SHIRT
    if current_shirt:
        screen.blit(current_shirt, (250, 100))

    # BUTTON
    pygame.draw.rect(screen, (0, 0, 255), shirt_button)

    # UPDATE SCREEN
    pygame.display.update()


# MAIN
def main():

    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Tuppence Dress Up")

    clock = pygame.time.Clock()

    # LOAD IMAGES
    body, shirt1 = load_images()

    # CURRENT CLOTHES
    current_shirt = None

    # BUTTONS
    shirt_button = pygame.Rect(50, 50, 100, 50)

    running = True

    while running:

        # HANDLE INPUT
        running, current_shirt = handle_events(
            shirt_button,
            shirt1,
            current_shirt
        )

        # DRAW FRAME
        draw_game(
            screen,
            body,
            current_shirt,
            shirt_button
        )

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()