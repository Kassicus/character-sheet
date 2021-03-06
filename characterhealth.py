import pygame
import textlabel
import textfield
import checkbox

class CharacterHealth():
    def __init__(self):
        self.x = 40
        self.y = 455

        self.armorClassField = textfield.TextField(self.x, self.y, 50, 30, "armor_class_field", fontSize = 24, alignment = "centered")  
        self.armorClassLabel = textlabel.TextLabel(self.x, self.y - 25, "AC")   
        self.armorClassLabel.x = int((self.x + 25) - (self.armorClassLabel.getWidth() / 2))

        self.initiativeField = textfield.TextField(self.x + 75, self.y, 50, 30, "initiative_field", fontSize = 24, alignment = "centered")
        self.initiativeLabel = textlabel.TextLabel(self.x + 75, self.y - 25, "Initiative")
        self.initiativeLabel.x = int((self.x + 100) - (self.initiativeLabel.getWidth() / 2))

        self.speedField = textfield.TextField(self.x + 150, self.y, 50, 30, "speed_field", fontSize = 24, alignment = "centered")
        self.speedLabel = textlabel.TextLabel(self.x + 150, self.y - 25, "Speed")
        self.speedLabel.x = int((self.x + 175) - (self.speedLabel.getWidth() / 2))

        self.maxHitPointLabel = textlabel.TextLabel(self.x + 5, self.y + 55, "Hit Point Max")
        self.maxHitPointField = textfield.TextField(self.x + self.maxHitPointLabel.getWidth() + 15, self.y + 55, 75, 15, "max_hit_points_field", "line", alignment = "centered")

        self.currentHitPointField = textfield.TextField(int(self.x + 103) - 78, self.y + 90, 150, 50, "current_hit_points_field", "line", 48, "centered")
        self.currentHitPointLabel = textlabel.TextLabel(self.x, self.y + 150, "Current Hit Points")
        self.currentHitPointLabel.x = int((self.x + 103) - ((self.currentHitPointLabel.getWidth() / 2) + 3))

        self.tempHitPointField = textfield.TextField(int(self.x + 103) - 78, self.y + 180, 150, 30, "temporary_hit_points_field", "line", 24, "centered")
        self.tempHitPointLabel = textlabel.TextLabel(self.x, self.y + 220, "Temporary Hit Points")
        self.tempHitPointLabel.x = int((self.x + 103) - ((self.tempHitPointLabel.getWidth() / 2) + 3))

        self.successCountLabel = textlabel.TextLabel(self.x + 5, self.y + 250, "Successes")
        self.successBox1 = checkbox.CheckBox(self.x + self.successCountLabel.getWidth() + 20, self.y + 250, "death_saving_success_one")
        self.successBox2 = checkbox.CheckBox(self.x + self.successCountLabel.getWidth() + 55, self.y + 250, "death_saving_success_two")
        self.successBox3 = checkbox.CheckBox(self.x + self.successCountLabel.getWidth() + 90, self.y + 250, "death_saving_success_three")
        
        self.failureCountLabel = textlabel.TextLabel(self.x + 5, self.y + 285, "Failures")
        self.failureBox1 = checkbox.CheckBox(self.x + self.successCountLabel.getWidth() + 20, self.y + 285, "death_saving_failure_one")
        self.failureBox2 = checkbox.CheckBox(self.x + self.successCountLabel.getWidth() + 55, self.y + 285, "death_saving_failure_two")
        self.failureBox3 = checkbox.CheckBox(self.x + self.successCountLabel.getWidth() + 90, self.y + 285, "death_saving_failure_three")

    def draw(self, surface):
        self.armorClassLabel.draw(surface)
        self.armorClassField.draw(surface)

        self.initiativeLabel.draw(surface)
        self.initiativeField.draw(surface)

        self.speedLabel.draw(surface)
        self.speedField.draw(surface)

        self.maxHitPointLabel.draw(surface)
        self.maxHitPointField.draw(surface)

        self.currentHitPointLabel.draw(surface)
        self.currentHitPointField.draw(surface)

        self.tempHitPointLabel.draw(surface)
        self.tempHitPointField.draw(surface)

        self.successCountLabel.draw(surface)
        self.successBox1.draw(surface)
        self.successBox2.draw(surface)
        self.successBox3.draw(surface)

        self.failureCountLabel.draw(surface)
        self.failureBox1.draw(surface)
        self.failureBox2.draw(surface)
        self.failureBox3.draw(surface)

        pygame.draw.rect(surface, (63, 58, 114), (self.x - 2, self.y + 50, 206, 275), 1)

    def update(self, events):
        self.armorClassField.update(events)
        self.initiativeField.update(events)
        self.speedField.update(events)
        self.maxHitPointField.update(events)
        self.currentHitPointField.update(events)
        self.tempHitPointField.update(events)

        self.successBox1.update(events)
        self.successBox2.update(events)
        self.successBox3.update(events)

        self.failureBox1.update(events)
        self.failureBox2.update(events)
        self.failureBox3.update(events)

    def save(self):
        self.armorClassField.save()
        self.initiativeField.save()
        self.speedField.save()
        self.maxHitPointField.save()
        self.currentHitPointField.save()
        self.tempHitPointField.save()

        self.successBox1.save()
        self.successBox2.save()
        self.successBox3.save()

        self.failureBox1.save()
        self.failureBox2.save()
        self.failureBox3.save()

    def load(self):
        self.armorClassField.load()
        self.initiativeField.load()
        self.speedField.load()
        self.maxHitPointField.load()
        self.currentHitPointField.load()
        self.tempHitPointField.load()

        self.successBox1.load()
        self.successBox2.load()
        self.successBox3.load()

        self.failureBox1.load()
        self.failureBox2.load()
        self.failureBox3.load()