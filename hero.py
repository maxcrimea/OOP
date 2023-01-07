class SuperHero:
    people = 'people'
    """Главный класс"""

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def show_name(self):
        print(f'Name: {self.name}')

    def mul(self):
        return self.health_points * 2

    def __str__(self):
        return f'{self.nickname} {self.superpower} {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)


Ironmane = SuperHero('Flasher', 'Flash', 'Freeze', 100,
                 'I am Flash')  # передал значения в объект класса для проверки работы кода

Ironmane.show_name()
print(Ironmane.mul())
print(Ironmane)
print(len(Ironmane))


class Hero2(SuperHero):
    costume = True
    """Класс супергероя Iron Man"""

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = False
        self.fly = False

    def mul(self):
        self.fly = True
        return pow(self.health_points, 2)

    def view_fly(self):
        print('fly in the True_phrase')


Ironmane = Hero2('Tony Stark', 'Iron Man', 'fly & power', 100, 'I am Iron Man!', 50, 'fly')
print(Ironmane.mul())
Ironmane.view_fly()
print(Ironmane)


class Hero3(SuperHero):
    cape = True
    """Класс супергероя Супермен"""

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = False
        self.fly = False

    def mul(self):
        self.fly = True
        return pow(self.health_points, 2)

    def view_fly(self):
        print('fly in the True_phrase')


Superman = Hero3('Kal-El', 'Superman', 'very strong', 100, 'a job for Superman', 70, 'fly')
print(Superman.mul())
Superman.view_fly()
print(Superman)


class villain(Hero3):
    people = 'monster'

    def gen_x(self):
        return None

    def crit(self):
        return pow(self.damage, 3)


Beast = villain('Hank', 'Beast', 'Superhuman strength', 100, 'I am The Beast', 75, 'fly')
print(Beast)
print(villain.crit(Superman))
