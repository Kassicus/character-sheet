import pygame
import button

class InfoPanel():
    def __init__(self, width, height, imagepath, name):
        """
        The infopanel class opens a new 'window' on the screen containing an image.
        imagepath: the str() containing the location of the image that needs to be render in the infopanel.
        name: the actual name of the infopanel, used for saving the infopanel data.
        """
        self.width = width
        self.height = height
        
        self.x = int((1500 / 2) - (self.width / 2))
        self.y = int((800 / 2) - (self.height / 2))

        self.name = name

        self.image = pygame.image.load(imagepath)

        self.isDrawn = False

        self.closeButton = button.Button(self.x + self.width - 11, self.y - 10, 10, 10, (255, 0, 0), self.deactivate)

    def draw(self, surface):
        if self.isDrawn:
            pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y - 11, self.width, 11), 0)
            pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.width, self.height), 1)

            self.closeButton.draw(surface)

            surface.blit(self.image, (self.x, self.y))

    def update(self, events):
        if self.isDrawn:
            self.closeButton.update(events)

    def deactivate(self):
        self.isDrawn = False

    def activate(self):
        self.isDrawn = True
