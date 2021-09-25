import pygame
import pickle

class Line(object):
    def __init__(self, x, y, content, lineId):
        self.x = x
        self.y = y

        self.content = content
        self.id = lineId

        self.font = pygame.font.Font("assets/fonts/gemunu/GemunuLibre-Regular.ttf", 16)
        self.renderedContent = self.font.render(self.content, True, (255, 255, 255))

    def draw(self, surface):
        surface.blit(self.renderedContent, (self.x, self.y))

    def update(self):
        self.renderedContent = self.font.render(self.content, True, (255, 255, 255))

    def save(self):
        pickle.dump(self.self.content, open(str("assets/data/textfields/" + "multi_line_text_" + str(self.id) + ".p"), "wb+"))

    def load(self):
        try:
            self.content = pickle.load(open(str("assets/data/textfields/" + "multi_line_text_" + str(self.id) + ".p"), "rb"))
        except:
            pass

class MultiLineTextField():
    def __init__(self, x, y, name):
        self.x = x
        self.y = y

        self.name = name

        self.x_step = self.y
        self.lineCount = 0

        self.lines = []
        self.currentLine = None

        self.createNewLine()

    def draw(self, surface):
        for line in self.lines:
            line.draw(surface)

    def update(self, events):
        self.getKeyboardInput(events)

        for line in self.lines:
            line.update()

        pygame.display.update()
        self.clock.tick(30)

    def getKeyboardInput(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.checkLine()
                elif event.key == pygame.K_RETURN:
                    self.createNewLine()
                else:
                    self.currentLine.content += event.unicode

    def createNewLine(self):
        x = Line(self.x, self.x_step, "", self.lineCount)

        self.lines.append(x)

        self.currentLine = self.lines[int(len(self.lines) - 1)]

        self.x_step += 20
        self.lineCount += 1

    def checkLine(self):
        if len(self.currentLine.content) == 0:
            self.lines.remove(self.lines[int(len(self.lines) - 1)])

            self.currentLine = self.lines[int(len(self.lines) - 1)]

            self.x_step -= 20
            self.lineCount -= 1
        else:
            self.currentLine.content = self.currentLine.content[:-1]