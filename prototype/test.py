from prototype.military_factory import MilitaryFactory


class Test:
    factory = MilitaryFactory()

    normal_soldier = factory.create_soldier()
    normal_soldier_2 = factory.create_soldier('blue', 3)

    print(normal_soldier.side)
    print(normal_soldier.rank)
    print(normal_soldier_2.side)
    print(normal_soldier_2.rank)
    print(normal_soldier_2.weapon.bullet)
    print(normal_soldier_2.weapon.weapon_type)


