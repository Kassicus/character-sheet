import pygame
import textfield
import textlabel
import checkbox
import infopanel
import button

pygame.init()
pygame.font.init()

class CharacterSheet():
    def __init__(self):
        self.screen = pygame.display.set_mode([1500, 800])
        pygame.display.set_caption("D&D Character Sheet")

        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

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

    def update(self):
        pygame.display.update()
        self.clock.tick(30)

cs = CharacterSheet()

cs.start()

pygame.quit()
