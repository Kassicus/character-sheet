import pygame

class TextLabel():
    def __init__(self, x, y, value, name):
        """
        The textlabel draws a static label on the screen.
        value: the actual text that will be displayed in the label.
        name: the name of the textlabel, used for saving textlabel data.
        """
        self.x = x
        self.y = y

        self.value = value

        self.font = pygame.font.Font('assets/fonts/ubuntu/Ubuntu-Regular.ttf', 16)

        self.text = self.font.render(self.value, True, (255, 255, 255))

        self.name = name

    def draw(self, surface):
        surface.blit(self.text, (self.x, self.y))

    def getWidth(self):
        return self.text.get_width()
