import pygame


# LOAD IMAGES
def load_images():
    background = [
        pygame.transform.scale(
            pygame.image.load("src/images/Background.png").convert(),
            (1410, 850)
        )
    ]

    body = pygame.image.load("src/images/Base.png").convert_alpha()

    tights = pygame.image.load("src/images/Tights.png").convert_alpha()

    dresses = [
        pygame.image.load("src/images/Dress1.png").convert_alpha(),
        pygame.image.load("src/images/Dress2.png").convert_alpha(),
        pygame.image.load("src/images/Dress3.png").convert_alpha(),
        pygame.image.load("src/images/Dress4.png").convert_alpha()
    ]

    shoes = [
        pygame.image.load("src/images/Shoes1.png").convert_alpha(),
        pygame.image.load("src/images/Shoes2.png").convert_alpha(),
        pygame.image.load("src/images/Shoes3.png").convert_alpha(),
        pygame.image.load("src/images/Shoes4.png").convert_alpha()
    ]

    return body, dresses, shoes, background, tights


# HANDLE EVENTS
def handle_events(
    dress_buttons,
    shoe_buttons,
    background_buttons,
    tights_buttons,
    dresses,
    shoes,
    background,
    tights,
    current_dress,
    current_shoes,
    current_background,
    save_button,
    current_tights
):
    running = True

    for event in pygame.event.get():

        # CLOSE WINDOW
        if event.type == pygame.QUIT:
            running = False

        # MOUSE CLICK
        if event.type == pygame.MOUSEBUTTONDOWN:

            # SAVE BUTTON
            if save_button.collidepoint(event.pos):
                filename = "outfit.png"
                pygame.image.save(pygame.display.get_surface(), filename)
                print("Outfit saved as", filename)

            # DRESS BUTTONS
            for i in range(len(dress_buttons)):
                if dress_buttons[i].collidepoint(event.pos):
                    current_dress = dresses[i]

            # SHOE BUTTONS
            for i in range(len(shoe_buttons)):
                if shoe_buttons[i].collidepoint(event.pos):
                    current_shoes = shoes[i]

            # BACKGROUND BUTTONS
            for i in range(len(background_buttons)):
                if background_buttons[i].collidepoint(event.pos):
                    current_background = background[i]

            # TIGHTS BUTTONS
            for button in tights_buttons:
                if button.collidepoint(event.pos):
                    current_tights = None if current_tights else tights

    return (
        running,
        current_dress,
        current_shoes,
        current_background,
        current_tights
    )


# DRAW EVERYTHING
def draw_game(
    screen,
    body,
    current_dress,
    current_shoes,
    current_background,
    current_tights,
    dress_buttons,
    shoe_buttons,
    background_buttons,
    tights_buttons,
    save_button
):
    # BACKGROUND
    if current_background:
        screen.blit(current_background, (-700, 0))

    # CHARACTER BASE
    screen.blit(body, (150, -270))

    # TIGHTS
    if current_tights:
        screen.blit(current_tights, (150, -270))

    # DRESS
    if current_dress:
        screen.blit(current_dress, (150, -270))

    # SHOES
    if current_shoes:
        screen.blit(current_shoes, (150, -270))

    # DRESS BUTTONS
    for button in dress_buttons:
        pygame.draw.rect(screen, (119, 49, 46), button)

    # SHOE BUTTONS
    for button in shoe_buttons:
        pygame.draw.rect(screen, (84, 14, 14), button)

    # TIGHTS BUTTONS
    for button in tights_buttons:
        pygame.draw.rect(screen, (117, 91, 72), button)

    # SAVE BUTTON
    pygame.draw.rect(screen, (209, 82, 137), save_button)
    font = pygame.font.SysFont(None, 24)
    text = font.render("SAVE", True, (255, 255, 255))
    screen.blit(text, (save_button.x + 30, save_button.y + 10))

    pygame.display.update()


# MAIN
def main():
    pygame.init()

    screen = pygame.display.set_mode((700, 850))
    pygame.display.set_caption("Tuppence Dress Up")

    clock = pygame.time.Clock()

    # LOAD ASSETS
    body, dresses, shoes, background, tights = load_images()

    # CURRENT STATE
    current_dress = None
    current_shoes = None
    current_background = background[0]
    current_tights = None

    # BUTTONS
    dress_buttons = [
        pygame.Rect(50, 50, 80, 40),
        pygame.Rect(50, 100, 80, 40),
        pygame.Rect(50, 150, 80, 40),
        pygame.Rect(50, 200, 80, 40)
    ]

    background_buttons = [
        pygame.Rect(250, 50, 80, 40)
    ]

    tights_buttons = [
        pygame.Rect(250, 120, 80, 40)
    ]

    shoe_buttons = [
        pygame.Rect(150, 50, 80, 40),
        pygame.Rect(150, 100, 80, 40),
        pygame.Rect(150, 150, 80, 40),
        pygame.Rect(150, 200, 80, 40)
    ]

    save_button = pygame.Rect(50, 260, 120, 40)

    # GAME LOOP
    running = True

    while running:

        running, current_dress, current_shoes, current_background, current_tights = handle_events(
            dress_buttons,
            shoe_buttons,
            background_buttons,
            tights_buttons,
            dresses,
            shoes,
            background,
            tights,
            current_dress,
            current_shoes,
            current_background,
            save_button,
            current_tights
        )

        draw_game(
            screen,
            body,
            current_dress,
            current_shoes,
            current_background,
            current_tights,
            dress_buttons,
            shoe_buttons,
            background_buttons,
            tights_buttons,
            save_button
        )

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()