import profpanel

class CharacterProf():
    def __init__(self):
        self.strProf = profpanel.ProfPanel(300, 10, "strength")
        self.dexProf = profpanel.ProfPanel(300, 35, "dexterity")
        self.conProf = profpanel.ProfPanel(300, 60, "constitution")
        self.intProf = profpanel.ProfPanel(300, 85, "intelligence")
        self.wisProf = profpanel.ProfPanel(300, 110, "wisdom")
        self.chaProf = profpanel.ProfPanel(300, 135, "charisma")

    def draw(self, surface):
        self.strProf.draw(surface)
        self.dexProf.draw(surface)
        self.conProf.draw(surface)
        self.intProf.draw(surface)
        self.wisProf.draw(surface)
        self.chaProf.draw(surface)

    def update(self, events):
        self.strProf.update(events)
        self.dexProf.update(events)
        self.conProf.update(events)
        self.intProf.update(events)
        self.wisProf.update(events)
        self.chaProf.update(events)

    def save(self):
        self.strProf.save()
        self.dexProf.save()
        self.conProf.save()
        self.intProf.save()
        self.wisProf.save()
        self.chaProf.save()

    def load(self):
        self.strProf.load()
        self.dexProf.load()
        self.conProf.load()
        self.intProf.load()
        self.wisProf.load()
        self.chaProf.load()