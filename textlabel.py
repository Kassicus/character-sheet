import pygame

class TextLabel():
    def __init__(self, x, y, value):
        """
        The textlabel draws a static label on the screen.
        value: the actual text that will be displayed in the label.
        """
        self.x = x
        self.y = y

        self.value = value

        self.font = pygame.font.Font('assets/fonts/ubuntu/Ubuntu-Regular.ttf', 16)

        self.text = self.font.render(self.value, True, (150, 150, 150))

    def draw(self, surface):
        surface.blit(self.text, (self.x, self.y))

    def getWidth(self):
        return self.text.get_width()
