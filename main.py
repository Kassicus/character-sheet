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

        self.label = textlabel.TextLabel(25, 25, "Character Name", "cname_label")
        self.text = textfield.TextField(150, 25, 150, 20, "cname_text")

        self.checkbox = checkbox.CheckBox(100, 100)

        self.info = infopanel.InfoPanel(25, 300, 150, 150)
        self.openInfo = button.Button(450, 150, 10, 10, (0, 255, 0), self.info.open)

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

        self.label.draw(self.screen)
        self.text.draw(self.screen)

        self.checkbox.draw(self.screen)

        self.info.draw(self.screen)
        self.openInfo.draw(self.screen)

    def update(self):
        self.text.update(self.events)

        self.checkbox.update(self.events)

        self.info.update(self.events)
        self.openInfo.update(self.events)

        pygame.display.update()
        self.clock.tick(30)

cs = CharacterSheet()

cs.start()

pygame.quit()
