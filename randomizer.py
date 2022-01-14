import random


class Randomizer:
    names = ["Burak", "Yağız", "Ahmet", "Devrim", "Doruk", "Onur", "Şevval", "Nisa", "Berke", "Yaren"]
    departments = ["Computer Engineering", "Business Administration", "Chemistry", "Medicine", "Marketing"]

    def create_id(self):
        return random.randint(1, 10000)

    def create_name(self):
        random_int = random.randint(0, 9)
        return self.names[random_int]

    def create_dept(self):
        random_int = random.randint(0, 4)
        return self.departments[random_int]

    def create_year(self):
        random_int = random.randint(0, 5)
        return random_int
