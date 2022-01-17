import copy


class Weapon:
    def __init__(self, bullet, weapon_type):
        self.bullet = bullet
        self.weapon_type = weapon_type

    def get_bullet(self):
        return self.bullet

    def set_bullet(self, bullet):
        self.bullet = bullet

    def get_weapon_type(self):
        return self.weapon_type

    def set_weapon_type(self, weapon_type):
        self.weapon_type = weapon_type

    def clone(self):
        return copy.copy(self)
