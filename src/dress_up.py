import pygame


# LOAD IMAGES
def load_images():
    background = pygame.transform.scale(
        pygame.image.load("src/images/Background.png").convert(),
        (700, 850)
    )

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
    tights_buttons,
    dresses,
    shoes,
    tights,
    current_dress,
    current_shoes,
    current_tights,
    save_button
):
    running = True

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            # SAVE
            if save_button.collidepoint(event.pos):
                pygame.image.save(pygame.display.get_surface(), "outfit.png")
                print("Outfit saved as outfit.png")

            # DRESSES
            for i, button in enumerate(dress_buttons):
                if button.collidepoint(event.pos):
                    current_dress = dresses[i]

            # SHOES
            for i, button in enumerate(shoe_buttons):
                if button.collidepoint(event.pos):
                    current_shoes = shoes[i]

            # TIGHTS TOGGLE
            for button in tights_buttons:
                if button.collidepoint(event.pos):
                    current_tights = None if current_tights else tights

    return running, current_dress, current_shoes, current_tights


# DRAW EVERYTHING
def draw_game(
    screen,
    background,
    body,
    current_dress,
    current_shoes,
    current_tights,
    dress_buttons,
    shoe_buttons,
    tights_buttons,
    save_button,
    dress_labels,
    shoe_labels,
    tights_label
):

    # BACKGROUND
    screen.blit(background, (0, 0))

    # BASE CHARACTER
    screen.blit(body, (150, -270))

    # LAYERS
    if current_tights:
        screen.blit(current_tights, (150, -270))

    if current_dress:
        screen.blit(current_dress, (150, -270))

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

    font_small = pygame.font.SysFont(None, 24)
    save_text = font_small.render("SAVE", True, (255, 255, 255))
    screen.blit(save_text, (save_button.x + 30, save_button.y + 10))

    # LABELS ON BUTTONS
    font = pygame.font.SysFont(None, 20)

    for button, label in zip(dress_buttons, dress_labels):
        screen.blit(label, (button.x + 25, button.y + 10))

    for button, label in zip(shoe_buttons, shoe_labels):
        screen.blit(label, (button.x + 25, button.y + 10))

    for button in tights_buttons:
        screen.blit(tights_label, (button.x + 30, button.y + 10))

    pygame.display.update()


# MAIN
def main():
    pygame.init()

    screen = pygame.display.set_mode((700, 850))
    pygame.display.set_caption("Tuppence Dress Up")
    clock = pygame.time.Clock()

    # ASSETS
    body, dresses, shoes, background, tights = load_images()

    # STATE
    current_dress = None
    current_shoes = None
    current_tights = None

    # BUTTONS
    dress_buttons = [
        pygame.Rect(50, 50, 80, 40),
        pygame.Rect(50, 100, 80, 40),
        pygame.Rect(50, 150, 80, 40),
        pygame.Rect(50, 200, 80, 40)
    ]

    shoe_buttons = [
        pygame.Rect(150, 50, 80, 40),
        pygame.Rect(150, 100, 80, 40),
        pygame.Rect(150, 150, 80, 40),
        pygame.Rect(150, 200, 80, 40)
    ]

    tights_buttons = [
        pygame.Rect(250, 120, 80, 40)
    ]

    save_button = pygame.Rect(50, 260, 120, 40)

    # LABELS
    font = pygame.font.SysFont(None, 20)

    dress_labels = [font.render(f"Dress{i+1}", True, (255, 255, 255)) for i in range(4)]
    shoe_labels = [font.render(f"Shoes{i+1}", True, (255, 255, 255)) for i in range(4)]
    tights_label = font.render("Tights", True, (255, 255, 255))

    # LOOP
    running = True

    while running:

        running, current_dress, current_shoes, current_tights = handle_events(
            dress_buttons,
            shoe_buttons,
            tights_buttons,
            dresses,
            shoes,
            tights,
            current_dress,
            current_shoes,
            current_tights,
            save_button
        )

        draw_game(
            screen,
            background,
            body,
            current_dress,
            current_shoes,
            current_tights,
            dress_buttons,
            shoe_buttons,
            tights_buttons,
            save_button,
            dress_labels,
            shoe_labels,
            tights_label
        )

        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
