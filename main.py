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

        self.characterNameLabel = textlabel.TextLabel(10, 10, "Character Name", "character_name_label")
        self.characterNameField = textfield.TextField(int(20 + self.characterNameLabel.getWidth()), 10, 120, 15, "character_name_field", "line")

        self.classAndLevelLabel = textlabel.TextLabel(10, 35, "Class & Level", "class_and_level_label")
        self.classAndLevelField = textfield.TextField(int(20 + self.classAndLevelLabel.getWidth()), 35, 120, 15, "class_and_level_field", "line")

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

        # Draw everything below this

        self.characterNameLabel.draw(self.screen)
        self.characterNameField.draw(self.screen)

        self.classAndLevelLabel.draw(self.screen)
        self.classAndLevelField.draw(self.screen)

    def update(self):
        self.characterNameField.update(self.events)
        self.classAndLevelField.update(self.events)

        # Update everthing above this

        pygame.display.update()
        self.clock.tick(30)

cs = CharacterSheet()

cs.start()

pygame.quit()
