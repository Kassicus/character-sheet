import pygame

class CheckBox():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.width = 20
        self.height = 20

        self.checked = False

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.width, self.height), 1)

        if self.checked:
            pygame.draw.rect(surface, (255, 255, 255), (self.x + 2, self.y + 2, self.width - 4, self.height - 4), 0)

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
