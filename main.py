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

        self.characterNameLabel = textlabel.TextLabel(10, 10, "Character Name")
        self.characterNameField = textfield.TextField(int(20 + self.characterNameLabel.getWidth()), 10, 120, 15, "character_name_field", "line")

        self.classAndLevelLabel = textlabel.TextLabel(10, 35, "Class & Level")
        self.classAndLevelField = textfield.TextField(int(20 + self.classAndLevelLabel.getWidth()), 35, 120, 15, "class_and_level_field", "line")

        self.raceLabel = textlabel.TextLabel(10, 60, "Race")
        self.raceField = textfield.TextField(int(20 + self.raceLabel.getWidth()), 60, 120, 15, "character_race_field", "line")

        self.backgroundLabel = textlabel.TextLabel(10, 85, "Background")
        self.backgroundField = textfield.TextField(int(20 + self.backgroundLabel.getWidth()), 85, 120, 15, "character_background_field", "line")

        self.alignmentLabel = textlabel.TextLabel(10, 110, "Alignment")
        self.alignmentField = textfield.TextField(int(20 + self.alignmentLabel.getWidth()), 110, 120, 15, "alignment_field", "line")

        self.experiencePointsLabel = textlabel.TextLabel(10, 135, "Experience Points")
        self.experiencePointsField = textfield.TextField(int(20 + self.experiencePointsLabel.getWidth()), 135, 120, 15, "experience_points_field", "line")

        self.strengthScoreLabel = textlabel.TextLabel(350, 10, "Strength")
        self.strengthScoreField = textfield.TextField(int(self.strengthScoreLabel.x + (self.strengthScoreLabel.getWidth() / 2) - 30 ),
        35, 60, 60, "strength_score_field", fontSize = 48, alignment = "centered")
        self.strengthModifierField = textfield.TextField(int(self.strengthScoreLabel.x + (self.strengthScoreLabel.getWidth() / 2) - 30),
        100, 60, 15, "strength_modifier_field", alignment = "centered")

        self.dexterityScoreLabel = textlabel.TextLabel(425, 10, "Dexterity")
        self.dexterityScoreField = textfield.TextField(int(self.dexterityScoreLabel.x + (self.dexterityScoreLabel.getWidth() / 2) - 30 ), 
        35, 60, 60, "dexterity_score_field", fontSize = 48, alignment = "centered")
        self.dexterityModifierField = textfield.TextField(int(self.dexterityScoreLabel.x + (self.dexterityScoreLabel.getWidth() / 2) - 30),
        100, 60, 15, "dexterity_modifier_field", alignment = "centered")

    def start(self):
        self.load()

        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.save()
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

        self.raceLabel.draw(self.screen)
        self.raceField.draw(self.screen)

        self.backgroundLabel.draw(self.screen)
        self.backgroundField.draw(self.screen)

        self.alignmentLabel.draw(self.screen)
        self.alignmentField.draw(self.screen)

        self.experiencePointsLabel.draw(self.screen)
        self.experiencePointsField.draw(self.screen)

        self.strengthScoreLabel.draw(self.screen)
        self.strengthScoreField.draw(self.screen)
        self.strengthModifierField.draw(self.screen)

        self.dexterityScoreLabel.draw(self.screen)
        self.dexterityScoreField.draw(self.screen)
        self.dexterityModifierField.draw(self.screen)


    def update(self):
        self.characterNameField.update(self.events)
        self.classAndLevelField.update(self.events)
        self.raceField.update(self.events)
        self.backgroundField.update(self.events)
        self.alignmentField.update(self.events)
        self.experiencePointsField.update(self.events)
        self.strengthScoreField.update(self.events)
        self.strengthModifierField.update(self.events)
        self.dexterityScoreField.update(self.events)
        self.dexterityModifierField.update(self.events)

        # Update everthing above this
        pygame.display.update()
        self.clock.tick(30)

    def save(self):
        self.characterNameField.save()
        self.classAndLevelField.save()
        self.raceField.save()
        self.backgroundField.save()
        self.alignmentField.save()
        self.experiencePointsField.save()
        self.strengthScoreField.save()
        self.strengthModifierField.save()
        self.dexterityScoreField.save()
        self.dexterityModifierField.save()

    def load(self):
        self.characterNameField.load()
        self.classAndLevelField.load()
        self.raceField.load()
        self.backgroundField.load()
        self.alignmentField.load()
        self.experiencePointsField.load()
        self.strengthScoreField.load()
        self.strengthModifierField.load()
        self.dexterityScoreField.load()
        self.dexterityModifierField.load()

cs = CharacterSheet()

cs.start()

pygame.quit()
