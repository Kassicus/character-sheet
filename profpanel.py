import textlabel
import textfield
import checkbox

class ProfPanel():
    def __init__(self, x, y, profName):
        """
        profpanel creates the three elements required to create a proficiency and handles them as one.
        profName: the name of the proficiency (must be lowercase)
        """
        self.x = x
        self.y = y

        self.profName = profName

        self.scoreCheckBox = checkbox.CheckBox(self.x, self.y, str(self.profName) + "_checkbox")

        self.scoreField = textfield.TextField(self.x + 30, self.y, 30, 15, str(self.profName + "_proficiency_field"), "line", alignment = "centered")

        self.scoreLabel = textlabel.TextLabel(self.x + 40 + self.scoreField.width, self.y, str(self.profName).capitalize())

    def draw(self, surface):
        self.scoreCheckBox.draw(surface)
        self.scoreField.draw(surface)
        self.scoreLabel.draw(surface)

    def update(self, events):
        self.scoreCheckBox.update(events)
        self.scoreField.update(events)

    def save(self):
        self.scoreCheckBox.save()
        self.scoreField.save()

    def load(self):
        self.scoreCheckBox.load()
        self.scoreField.load()