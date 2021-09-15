import pygame

class TextField():
    def __init__(self, x, y, width, height, name):
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.name = str(name)

        self.focused = False

        self.font = pygame.font.Font('assets/fonts/ubuntu/Ubuntu-Regular.ttf', 16)

        self.text = ""

        self.renderedText = self.font.render(self.text, True, (255, 255, 255))

    def draw(self, surface):
        if self.focused:
            pygame.draw.rect(surface, (0, 255, 0), (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 1)
        else:
            pygame.draw.rect(surface, (255, 255, 255), (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 1)

        surface.blit(self.renderedText, (self.x, self.y))

    def update(self, events):
        self.checkFocused(events)

        self.renderedText = self.font.render(self.text, True, (255, 255, 255))

        if self.focused:
            self.getKeyboardInput(events)

    def checkFocused(self, events):
        pos = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.x <= pos[0] <= self.x + self.width:
                    if self.y <= pos[1] <= self.y + self.height:
                        self.focused = True
                    else:
                        self.focused = False
                else:
                    self.focused = False

    def getKeyboardInput(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.focused = False
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
