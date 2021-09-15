import pygame

class TextLabel():
    def __init__(self, x, y, value, name):
        self.x = x
        self.y = y

        self.value = value

        self.font = pygame.font.Font('assets/fonts/ubuntu/Ubuntu-Regular.ttf', 16)

        self.text = self.font.render(self.value, True, (255, 255, 255))

        self.name = name

    def draw(self, surface):
        surface.blit(self.text, (self.x, self.y))
