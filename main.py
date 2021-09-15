import pygame
import text

pygame.init()
pygame.font.init()

class CharacterSheet():
    def __init__(self):
        self.screen = pygame.display.set_mode([1500, 800])
        pygame.display.set_caption("D&D Character Sheet")

        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

        self.text = text.Field(25, 25, 100, 50)
        self.text2 = text.Field(25, 100, 100, 50)

    def start(self):
        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill((0, 0, 0))

        self.text.draw(self.screen)
        self.text2.draw(self.screen)

    def update(self):
        self.text.update(self.events)
        self.text2.update(self.events)

        pygame.display.update()
        self.clock.tick(30)

cs = CharacterSheet()

cs.start()

pygame.quit()
