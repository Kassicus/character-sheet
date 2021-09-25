import pygame
import infopanel
import button
import characterinfo
import characterattr
import characterprof
import characterskill
import characterhealth
import toolbar

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
        self.characterHealth = characterhealth.CharacterHealth()

        self.toolbar = toolbar.Toolbar()

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
        self.screen.fill((34, 32, 52))

        # Draw everything below this
        self.characterInformation.draw(self.screen)
        self.characterAttributs.draw(self.screen)
        self.characterProficiencies.draw(self.screen)
        self.characterSkills.draw(self.screen)
        self.characterHealth.draw(self.screen)

        self.toolbar.draw(self.screen)

        # Draw all popups below this

    def update(self):
        self.characterInformation.update(self.events)
        self.characterAttributs.update(self.events)
        self.characterProficiencies.update(self.events)
        self.characterSkills.update(self.events)
        self.characterHealth.update(self.events)

        self.toolbar.update(self.events)

        # Update all popups below this

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
        self.characterHealth.save()

    def load(self):
        self.characterInformation.load()
        self.characterAttributs.load()
        self.characterProficiencies.load()
        self.characterSkills.load()
        self.characterHealth.load()

cs = CharacterSheet()

cs.start()

pygame.quit()
