import textlabel
import textfield

class AttrPanel():
    def __init__(self, x, y, attrName):
        """
        The attrpanel (attribute panel) creates the three elements required to create an attribute and handles them as one element
        attrName: the name of the attribute, ie 'strength' this must be lowercase
        """
        self.x = x
        self.y = y

        self.attrName = attrName

        self.width = 60
        self.height = 60

        self.scoreField = textfield.TextField(self.x, self.y + 25, self.width, self.height, str(self.attrName + "_score_field"), fontSize = 48, alignment = "centered")

        self.scoreLabel = textlabel.TextLabel(self.x, self.y, str(self.attrName).capitalize())
        self.scoreLabel.x = int(self.x + (self.width / 2) - (self.scoreLabel.getWidth() / 2))

        self.modifierField = textfield.TextField(self.x, self.y + 90, self.width, 15, str(self.attrName + "_modifier_field"), alignment = "centered")


    def draw(self, surface):
        self.scoreLabel.draw(surface)
        self.scoreField.draw(surface)
        self.modifierField.draw(surface)

    def update(self, events):
        self.scoreField.update(events)
        self.modifierField.update(events)

    def save(self):
        self.scoreField.save()
        self.modifierField.save()

    def load(self):
        self.scoreField.load()
        self.modifierField.load()