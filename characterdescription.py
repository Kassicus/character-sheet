import textlabel

class CharacterDescription():
    def __init__(self):
        self.x = 515
        self.y = 10

        self.personalityTraitLabel = textlabel.TextLabel(self.x, self.y, "Personality Traits")

    def draw(self, surface):
        self.personalityTraitLabel.draw(surface)