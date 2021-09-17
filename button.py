import pygame

class Button():
    def __init__(self, x, y, width, height, color, function, name):
        """
        The button class draws a interactable button on screen.
        function: a function of the parent of the button, called when the button is clicked.
        name: the actual name of the button, used for saving button data
        """
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.name = name

        self.color = color

        self.function = function

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height), 0)

    def update(self, events):
        self.checkClicked(events)

    def checkClicked(self, events):
        pos = pygame.mouse.get_pos()

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.x <= pos[0] <= self.x + self.width:
                    if self.y <= pos[1] <= self.y + self.height:
                        self.function()
