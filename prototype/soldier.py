import copy


class Soldier:
    def __init__(self, side, rank, weapon, power):
        self.side = side
        self.rank = rank
        self.weapon = weapon
        self.power = power

    def get_side(self):
        return self.side

    def set_side(self, side):
        self.side = side

    def get_rank(self):
        return self.rank

    def set_rank(self, rank):
        self.rank = rank

    def get_weapon(self):
        return self.weapon

    def set_weapon(self, weapon):
        self.weapon = weapon

    def get_power(self):
        return self.power

    def set_power(self, power):
        self.power = power

    def clone(self):
        return copy.copy(self)


