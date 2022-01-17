import copy


class Military:
    def __init__(self, color, leader, soldier, weapon, vehicle):
        self.color = color
        self.leader = leader
        self.soldier = soldier
        self.weapon = weapon
        self.vehicle = vehicle

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_leader(self):
        return self.leader

    def set_leader(self, leader):
        self.leader = leader

    def get_soldier(self):
        return self.soldier

    def set_soldier(self, soldier):
        self.soldier = soldier

    def get_weapon(self):
        return self.weapon

    def set_weapon(self, weapon):
        self.weapon = weapon

    def get_vehicle(self):
        return self.vehicle

    def set_vehicle(self, vehicle):
        self.vehicle = vehicle
