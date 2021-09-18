import attrpanel

class CharacterAttr():
    def __init__(self):
        self.strAttr = attrpanel.AttrPanel(20, 180, "strength")
        self.dexAttr = attrpanel.AttrPanel(110, 180, "dexterity")
        self.conAttr = attrpanel.AttrPanel(200, 180, "constitution")
        self.intAttr = attrpanel.AttrPanel(20, 300, "intelligence")
        self.wisAttr = attrpanel.AttrPanel(110, 300, "wisdom")
        self.chaAttr = attrpanel.AttrPanel(200, 300, "charisma")

    def draw(self, surface):
        self.strAttr.draw(surface)
        self.dexAttr.draw(surface)
        self.conAttr.draw(surface)
        self.intAttr.draw(surface)
        self.wisAttr.draw(surface)
        self.chaAttr.draw(surface)

    def update(self, events):
        self.strAttr.update(events)
        self.dexAttr.update(events)
        self.conAttr.update(events)
        self.intAttr.update(events)
        self.wisAttr.update(events)
        self.chaAttr.update(events)

    def save(self):
        self.strAttr.save()
        self.dexAttr.save()
        self.conAttr.save()
        self.intAttr.save()
        self.wisAttr.save()
        self.chaAttr.save()

    def load(self):
        self.strAttr.load()
        self.dexAttr.load()
        self.conAttr.load()
        self.intAttr.load()
        self.wisAttr.load()
        self.chaAttr.load()