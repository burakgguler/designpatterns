import copy


class Vehicle:
    def __init__(self, shoot_range, speed):
        self.shoot_range = shoot_range
        self.speed = speed

    def get_shoot_range(self):
        return self.shoot_range

    def set_shoot_range(self, shoot_range):
        self.shoot_range = shoot_range

    def get_speed(self):
        return self.speed

    def set_speed(self, speed):
        self.speed = speed

    def clone(self):
        return copy.copy(self)


