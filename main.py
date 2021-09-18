import pygame
import textfield
import textlabel
import checkbox
import infopanel
import button
import attrpanel

pygame.init()
pygame.font.init()

class CharacterSheet():
    def __init__(self):
        self.screen = pygame.display.set_mode([1500, 800])
        pygame.display.set_caption("D&D Character Sheet")

        self.running = True
        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

        self.debug = False

        self.characterNameLabel = textlabel.TextLabel(10, 10, "Character Name")
        self.characterNameField = textfield.TextField(140, 10, 120, 15, "character_name_field", "line")

        self.classAndLevelLabel = textlabel.TextLabel(10, 35, "Class & Level")
        self.classAndLevelField = textfield.TextField(140, 35, 120, 15, "class_and_level_field", "line")

        self.raceLabel = textlabel.TextLabel(10, 60, "Race")
        self.raceField = textfield.TextField(140, 60, 120, 15, "character_race_field", "line")

        self.backgroundLabel = textlabel.TextLabel(10, 85, "Background")
        self.backgroundField = textfield.TextField(140, 85, 120, 15, "character_background_field", "line")

        self.alignmentLabel = textlabel.TextLabel(10, 110, "Alignment")
        self.alignmentField = textfield.TextField(140, 110, 120, 15, "alignment_field", "line")

        self.experiencePointsLabel = textlabel.TextLabel(10, 135, "EXP Points")
        self.experiencePointsField = textfield.TextField(140, 135, 120, 15, "experience_points_field", "line")

        self.strAttr = attrpanel.AttrPanel(295, 10, "strength")
        self.dexAttr = attrpanel.AttrPanel(395, 10, "dexterity")
        self.conAttr = attrpanel.AttrPanel(495, 10, "constitution")
        self.intAttr = attrpanel.AttrPanel(595, 10, "intelligence")
        self.wisAttr = attrpanel.AttrPanel(695, 10, "wisdom")
        self.chaAttr = attrpanel.AttrPanel(795, 10, "charisma")

        #self.test = infopanel.InfoPanel(1198, 591, "assets/data/spells/horrid_wilting.png", "test")
        #self.testbutton = button.Button(500, 500, 50, 50, (0, 255, 0), self.test.activate)

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

        self.strAttr.draw(self.screen)
        self.dexAttr.draw(self.screen)
        self.conAttr.draw(self.screen)
        self.intAttr.draw(self.screen)
        self.wisAttr.draw(self.screen)
        self.chaAttr.draw(self.screen)

        #self.testbutton.draw(self.screen)

        # Draw all popups below this
        #self.test.draw(self.screen)

    def update(self):
        self.characterNameField.update(self.events)
        self.classAndLevelField.update(self.events)
        self.raceField.update(self.events)
        self.backgroundField.update(self.events)
        self.alignmentField.update(self.events)
        self.experiencePointsField.update(self.events)

        self.strAttr.update(self.events)
        self.dexAttr.update(self.events)
        self.conAttr.update(self.events)
        self.intAttr.update(self.events)
        self.wisAttr.update(self.events)
        self.chaAttr.update(self.events)

        #self.testbutton.update(self.events)

        # Update all popups below this
        #self.test.update(self.events)

        # Update everthing above this
        if self.debug:
            print(pygame.mouse.get_pos())

        pygame.display.update()
        self.clock.tick(30)

    def save(self):
        self.characterNameField.save()
        self.classAndLevelField.save()
        self.raceField.save()
        self.backgroundField.save()
        self.alignmentField.save()
        self.experiencePointsField.save()

        self.strAttr.save()
        self.dexAttr.save()
        self.conAttr.save()
        self.intAttr.save()
        self.wisAttr.save()
        self.chaAttr.save()

    def load(self):
        self.characterNameField.load()
        self.classAndLevelField.load()
        self.raceField.load()
        self.backgroundField.load()
        self.alignmentField.load()
        self.experiencePointsField.load()

        self.strAttr.load()
        self.dexAttr.load()
        self.conAttr.load()
        self.intAttr.load()
        self.wisAttr.load()
        self.chaAttr.load()

cs = CharacterSheet()

cs.start()

pygame.quit()
