import textlabel
import textfield

class CharacterInfo():
    def __init__(self):
        self.characterNameLabel = textlabel.TextLabel(10, 10, "Character Name")
        self.characterNameField = textfield.TextField(140, 10, 120, 15, "character_name_field", "line")

        self.classAndLevelLabel = textlabel.TextLabel(10, 35, "Class & Level")
        self.classAndLevelField = textfield.TextField(140, 35, 120, 15, "class_and_level_field", "line")

        self.raceLabel = textlabel.TextLabel(10, 60, "Race")
        self.raceField = textfield.TextField(140, 60, 120, 15, "character_race_field", "line")

        self.backgroundLabel = textlabel.TextLabel(10, 85, "Background")
        self.backgroundField = textfield.TextField(140, 85, 120, 15, "character_background_field", "line")

        self.alignmentLabel = textlabel.TextLabel(10, 110, "Alignment")
        self.alignmentField = textfield.TextField(140, 110, 120, 15, "alignment_field", "line")

        self.experiencePointsLabel = textlabel.TextLabel(10, 135, "EXP Points")
        self.experiencePointsField = textfield.TextField(140, 135, 120, 15, "experience_points_field", "line")

    def draw(self, surface):
        self.characterNameLabel.draw(surface)
        self.characterNameField.draw(surface)

        self.classAndLevelLabel.draw(surface)
        self.classAndLevelField.draw(surface)

        self.raceLabel.draw(surface)
        self.raceField.draw(surface)

        self.backgroundLabel.draw(surface)
        self.backgroundField.draw(surface)

        self.alignmentLabel.draw(surface)
        self.alignmentField.draw(surface)

        self.experiencePointsLabel.draw(surface)
        self.experiencePointsField.draw(surface)

    def update(self, events):
        self.characterNameField.update(events)
        self.classAndLevelField.update(events)
        self.raceField.update(events)
        self.backgroundField.update(events)
        self.alignmentField.update(events)
        self.experiencePointsField.update(events)

    def save(self):
        self.characterNameField.save()
        self.classAndLevelField.save()
        self.raceField.save()
        self.backgroundField.save()
        self.alignmentField.save()
        self.experiencePointsField.save()

    def load(self):
        self.characterNameField.load()
        self.classAndLevelField.load()
        self.raceField.load()
        self.backgroundField.load()
        self.alignmentField.load()
        self.experiencePointsField.load()