import pygame
import pickle

class CheckBox():
    def __init__(self, x, y, name):
        """
        The checkbox class draws an interactable checkbox on screen.
        name: the actual name of the checkbox, used for saving checkbox data.
        """
        self.x = x
        self.y = y

        self.width = 20
        self.height = 20

        self.name = name

        self.checked = False

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.width, self.height), 1)

        if self.checked:
            pygame.draw.rect(surface, (255, 255, 255), (self.x + 3, self.y + 3, self.width - 6, self.height - 6), 0)

    def update(self, events):
        self.checkFocused(events)

    def checkFocused(self, events):
        pos = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.x <= pos[0] <= self.x + self.width:
                    if self.y <= pos[1] <= self.y + self.height:
                        if self.checked:
                            self.checked = False
                        else:
                            self.checked = True

    def save(self):
        pickle.dump(self.checked, open(str("assets/data/checkboxes/" + self.name + "_state.p").replace(" ", "_"), "wb+"))

    def load(self):
        try:
            self.checked = pickle.load(open(str("assets/data/checkboxes/" + self.name + "_state.p").replace(" ", "_"), "rb"))
        except:
            pass
