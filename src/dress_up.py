import pygame


# LOAD IMAGES
def load_images():

    body = pygame.image.load("src/images/Base.png").convert_alpha()
    tights = pygame.image.load("src/images/Tights.png")
    dresses = [
        pygame.image.load("src/images/Dress1.png")
        pygame.image.load("src/images/Dress2.png")
        pygame.image.load("src/images/Dress3.png")
        pygame.image.load("src/images/Dress4.png")
    ]
    
    shoes = [
        pygame.image.load("src/images/Shoes1.png")
        pygame.image.load("src/images/Shoes2.png")
        pygame.image.load("src/images/Shoes3.png")
        pygame.image.load("src/images/Shoes4.png")
        ]


    return body, dresses, shoes, tights


# HANDLE EVENTS
def handle_events(dress_button, dresses, current_dress):

    running = True

    for event in pygame.event.get():

        # CLOSE WINDOW
        if event.type == pygame.QUIT:
            running = False

        # MOUSE CLICK
        if event.type == pygame.MOUSEBUTTONDOWN:

            if dress_button.collidepoint(event.pos):

                current_dress = dresses

    return running, current_dress


# DRAW EVERYTHING
def draw_game(screen, body, current_dress, dress_button):

    # BACKGROUND
    screen.fill((255, 200, 200))

    # BODY
    screen.blit(body, (250, 100))

    # DRESS
    if current_dress:
        screen.blit(current_dress, (250, 100))

    # BUTTON
    pygame.draw.rect(screen, (0, 0, 255), dress_button)

    # UPDATE SCREEN
    pygame.display.update()


# MAIN
def main():

    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Tuppence Dress Up")

    clock = pygame.time.Clock()

    # LOAD IMAGES
    body, dresses = load_images()

    # CURRENT CLOTHES
    current_dress = None

    # BUTTONS
    dress_button = pygame.Rect(50, 50, 100, 50)

    running = True

    while running:

        # HANDLE INPUT
        running, current_dress = handle_events(
            dress_button,
            dress1,
            current_dress
        )

        # DRAW FRAME
        draw_game(
            screen,
            body,
            current_dress,
            dress_button
        )

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()