import pygame

class Button():
    def __init__(self, x, y, width, height, function, value = "", fontSize = 16, app = "generic"):
        """
        The button class draws a interactable button on screen.
        function: a function of the parent of the button, called when the button is clicked.
        """
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.color = (63, 58, 114)
        self.hoveredColor = (81, 255, 154)
        self.function = function

        self.hovered = False

        self.drawText = False

        self.font = pygame.font.Font('assets/fonts/ubuntu/Ubuntu-Regular.ttf', fontSize)
        self.value = value
        self.renderedValue = self.font.render(self.value, True, (150, 140, 235))

        self.app = app

        if self.value != "":
            self.drawText = True

    def draw(self, surface):
        if self.hovered:
            pygame.draw.rect(surface, self.hoveredColor, (self.x, self.y, self.width, self.height), 0)
            if self.app == "close":
                self.renderClose(surface, "hovered")
        else:
            pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height), 0)
            if self.app == "close":
                self.renderClose(surface)

        if self.drawText:
            surface.blit(self.renderedValue, (int(self.x + (self.width / 2)) - (self.renderedValue.get_width() / 2), self.y))

    def update(self, events):
        self.checkClicked(events)

        if self.hovered:
            self.renderedValue = self.font.render(self.value, True, (34, 32, 52))
        else:
            self.renderedValue = self.font.render(self.value, True, (150, 140, 235))

    def checkClicked(self, events):
        pos = pygame.mouse.get_pos()

        if self.x <= pos[0] <= self.x + self.width:
            if self.y <= pos[1] <= self.y + self.height:
                self.hovered = True
                for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.function()
            else:
                self.hovered = False
        else:
            self.hovered = False

    def renderClose(self, surface, app = ""):
        if app == "hovered":
            pygame.draw.line(surface, (34, 32, 52), (self.x + 2, self.y + 2), (self.x + self.width - 4, self.y + self.height - 4), 2)
            pygame.draw.line(surface, (34, 32, 52), (self.x + 2, self.y + self.height - 4), (self.x + self.width - 4, self.y + 2), 2)
        else:
            pygame.draw.line(surface, (150, 140, 235), (self.x + 2, self.y + 2), (self.x + self.width - 4, self.y + self.height - 4), 2)
            pygame.draw.line(surface, (150, 140, 235), (self.x + 2, self.y + self.height - 4), (self.x + self.width - 4, self.y + 2), 2)