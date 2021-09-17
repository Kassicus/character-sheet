import pygame
import button

class InfoPanel():
    def __init__(self, x, y, width, height, imagepath, name):
        """
        The infopanel class opens a new 'window' on the screen containing an image.
        imagepath: the str() containing the location of the image that needs to be render in the infopanel.
        name: the actual name of the infopanel, used for saving the infopanel data.
        """
        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.name = name

        self.image = pygame.image.load(imagepath)

        self.isDrawn = True

        self.closeButton = button.Button(self.x + self.width - 11, self.y - 10, 10, 10, (255, 0, 0), self.close)

    def draw(self, surface):
        if self.isDrawn:
            pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y - 11, self.width, 11), 0)
            pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.width, self.height), 1)

            self.closeButton.draw(surface)

    def update(self, events):
        if self.isDrawn:
            self.closeButton.update(events)

    def close(self):
        self.isDrawn = False

    def open(self):
        self.isDrawn = True
