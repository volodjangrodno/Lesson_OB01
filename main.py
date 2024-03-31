class Warrior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def sleep(self):
        print(f"{self.name} лёг спать")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 1

    def hit(self):
        print(f"{self.name} бьёт кого-то")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} гуляет")

    def info(self):
        print(f"Имя война - {self.name}")
        print(f"Цвет волос воина - {self.hair_color}")
        print(f"Сила воина - {self.power}")
        print(f"Выносливость воина - {self.endurance}")


war1 = Warrior(name="Стёпа", power=76, endurance=54, hair_color="коричневые")
war2 = Warrior(name="Егор", power=45, endurance=23, hair_color="блонд")

print(war1.name)
print(war1.power)
print(war1.endurance)
print(war1.hair_color)

print(war2.power)
print(war2.endurance)

war2.sleep()
war2.eat()
war1.hit()
war1.walk()

war1.info()
war2.info()