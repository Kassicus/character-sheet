import pygame
import pickle

class TextField():
    def __init__(self, x, y, width, height, name, drawType = "box", fontSize = 16, alignment = "left"):
        """
        The textfield draws an interactible text window on the screen for text to be input to.
        name: the name of the textfield, used for saving textfield data.
        drawType: (default 'box') the type of outline the field with be drawing with, 'box' or 'line'
        fontSize: (default 16) the size of the font used inside of the text field.
        """
        self.x = x
        self.y = y
        self.xoffset = 2
        self.yoffset = 2
        self.realx = self.x - self.xoffset
        self.realy = self.y - self.yoffset

        self.width = width
        self.height = height
        self.widthoffset = 6
        self.heightoffset = 6
        self.realwidth = self.width + self.widthoffset
        self.realheight = self.height + self.heightoffset

        self.name = str(name)

        self.focused = False

        self.font = pygame.font.Font('assets/fonts/ubuntu/Ubuntu-Regular.ttf', fontSize)

        self.text = ""

        self.renderedText = self.font.render(self.text, True, (255, 255, 255))

        self.drawType = drawType

        self.alignment = alignment

    def draw(self, surface):
        if self.focused:
            if self.drawType == "box":
                pygame.draw.rect(surface, (0, 255, 0), (self.realx, self.realy, self.realwidth, self.realheight), 1)
            elif self.drawType == "line":
                pygame.draw.line(surface, (0, 255, 0), (self.realx, self.y + self.realheight), (self.x + self.realwidth, self.y + self.realheight))
        else:
            if self.drawType == "box":
                pygame.draw.rect(surface, (255, 255, 255), (self.realx, self.realy, self.realwidth, self.realheight), 1)
            elif self.drawType == "line":
                pygame.draw.line(surface, (255, 255, 255), (self.realx, self.y + self.realheight), (self.x + self.realwidth, self.y + self.realheight))

        if self.alignment == "centered":
            surface.blit(self.renderedText, (int(self.x + (self.width / 2) - (self.renderedText.get_width() / 2)), self.y))
        elif self.alignment == "left":
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
                if self.realx <= pos[0] <= self.realx + self.realwidth:
                    if self.realy <= pos[1] <= self.realy + self.realheight:
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

    def getWidth(self):
        return self.renderedText.get_width()

    def save(self):
        pickle.dump(self.text, open(str("assets/data/textfields/" + self.name + "_text.p"), "wb+"))

    def load(self):
        try:
            self.text = pickle.load(open(str("assets/data/textfields/" + self.name + "_text.p"), "rb"))
        except:
            pass
