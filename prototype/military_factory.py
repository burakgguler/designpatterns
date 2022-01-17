



from prototype.factory import Factory
from prototype.military import Military
from prototype.soldier import Soldier
from prototype.vehicle import Vehicle
from prototype.weapon import Weapon
from multipledispatch import dispatch


class MilitaryFactory(Factory):
    @dispatch()
    def create_soldier(self) -> Soldier:
        soldier = self.MilitaryPrototypes.soldier_prototype.clone()
        return soldier

    @dispatch(str, int)
    def create_soldier(self, side, rank) -> Soldier:
        soldier = self.MilitaryPrototypes.soldier_prototype.clone()
        soldier.set_side(side)
        soldier.set_rank(rank)
        return soldier

    def create_red_soldier(self, rank) -> Soldier:
        soldier = self.MilitaryPrototypes.soldier_prototype.clone()
        soldier.set_rank(rank)
        return soldier

    def create_blue_soldier(self, rank) -> Soldier:
        soldier = self.MilitaryPrototypes.soldier_prototype.clone()
        soldier.set_rank(rank)
        soldier.set_side('blue')
        return soldier

    def create_weapon(self, bullet, weapon_type) -> Weapon:
        weapon = self.MilitaryPrototypes.weapon_prototype.clone()
        weapon.set_bullet(bullet)
        weapon.set_weapon_type(weapon_type)
        return weapon

    def create_vehicle(self, shoot_range, speed) -> Vehicle:
        vehicle = self.MilitaryPrototypes.vehicle_prototype.clone()
        vehicle.set_shoot_range(shoot_range)
        vehicle.set_speed(speed)
        return vehicle

    def create_military(self) -> Military:
        return super().create_military()

    class MilitaryPrototypes:
        soldier_prototype = Soldier('red', 2, Weapon(100, 'ak47'), 100)
        weapon_prototype = Weapon(500, 'm4a1')
        vehicle_prototype = Vehicle(2, 200)
