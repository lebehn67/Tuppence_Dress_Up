import pygame

def main():
    pygame.init()

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Tuppence Dress Up")

    clock = pygame.time.Clock()

    body = pygame.image.load("images/base.png")
    dress1 = pygame.image.load("images/Dress1.png")

    current_dress = None

    dress_button = pygame.Rect(50, 50, 100, 50)

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dress_button.collidepoint(event.pos):
                    current_dress = dress1


        screen.fill((255, 200, 200))

        screen.blit(body, (250, 100))
        if current_dress:
            screen.blit(dress1, (250, 100))

        pygame.draw.rect(screen, (0, 0, 255), dress_button)

        pygame.display.update()

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()