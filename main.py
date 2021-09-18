import pygame
import infopanel
import button
import characterinfo
import characterattr
import characterprof
import characterskill

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

        self.characterInformation = characterinfo.CharacterInfo()
        self.characterAttributs = characterattr.CharacterAttr()
        self.characterProficiencies = characterprof.CharacterProf()
        self.characterSkills = characterskill.CharacterSkill()

        self.test = infopanel.InfoPanel(1198, 591, "assets/data/spells/horrid_wilting.png", "test")
        self.testbutton = button.Button(500, 500, 50, 50, (0, 255, 0), self.test.activate)

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
        self.characterInformation.draw(self.screen)
        self.characterAttributs.draw(self.screen)
        self.characterProficiencies.draw(self.screen)
        self.characterSkills.draw(self.screen)

        self.testbutton.draw(self.screen)

        # Draw all popups below this
        self.test.draw(self.screen)

    def update(self):
        self.characterInformation.update(self.events)
        self.characterAttributs.update(self.events)
        self.characterProficiencies.update(self.events)
        self.characterSkills.update(self.events)

        self.testbutton.update(self.events)

        # Update all popups below this
        self.test.update(self.events)

        # Update everthing above this
        if self.debug:
            print(pygame.mouse.get_pos())

        pygame.display.update()
        self.clock.tick(30)

    def save(self):
        self.characterInformation.save()
        self.characterAttributs.save()
        self.characterProficiencies.save()
        self.characterSkills.save()

    def load(self):
        self.characterInformation.load()
        self.characterAttributs.load()
        self.characterProficiencies.load()
        self.characterSkills.load()

cs = CharacterSheet()

cs.start()

pygame.quit()
