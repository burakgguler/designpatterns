from prototype.military import Military
from prototype.soldier import Soldier
from prototype.vehicle import Vehicle
from prototype.weapon import Weapon
from multipledispatch import dispatch


class Factory:
    @dispatch()
    def create_soldier(self) -> Soldier:
        pass

    @dispatch(str, int)
    def create_soldier(self, side, rank) -> Soldier:
        pass

    def create_red_soldier(self, rank) -> Soldier:
        pass

    def create_blue_soldier(self, rank) -> Soldier:
        pass

    def create_weapon(self, bullet, weapon_type) -> Weapon:
        pass

    def create_vehicle(self, shoot_range, speed) -> Vehicle:
        pass

    def create_military(self) -> Military:
        pass
