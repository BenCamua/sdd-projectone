class Player(object):
    def __init__(self, name, alignment='neutral', health=100):
        self.name = name
        self.health = health
        self.alignment = alignment

    def hurt(self, health):
        if health <= 0
            return RuntimeError('Death')
        else:
            return health

    def heal(self, health):
