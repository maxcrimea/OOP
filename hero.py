class SuperHero:
    people = 'people'

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


Hero = SuperHero('Flasher', 'Flasher', 'Freeze', 100,
                 'I am Flash')  # передал значения в объект класса для проверки работы кода

Hero.show_name()
print(Hero.mul())
print(Hero)
print(len(Hero))


class SuperHero2(SuperHero):
    people1 = 'people1'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = False
        self.fly = False

    def mul(self):
        super().mul()
        self.fly = True
        return self.health_points ** 2

    def view_fly(self):
        print('fly in the True_phrase')

    def __str__(self):
        return f'{self.fly} {self.superpower} {self.health_points}'


Hero2 = SuperHero2('Flasher', 'Flasher', 'Freeze', 100, 'I am Flash', 50, 'fly')
print(Hero2.mul())
Hero2.view_fly()
print(Hero2)


class SuperHero3(SuperHero):
    people2 = 'people2'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = False
        self.fly = False

    def mul(self):
        super().mul()
        self.fly = True
        return self.health_points ** 2

    def view_fly(self):
        print('fly in the True_phrase')


Hero3 = SuperHero3('Flasher', 'Flasher', 'Freeze', 80, 'I am Flash', 70, 'fly')
print(Hero3.mul())
Hero3.view_fly()
print(Hero3)


class villain(SuperHero3):
    people = 'monster'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage, fly)

    def gen_x(self):
        return None

    def crit(self):
        return self.damage ** 2


vill = villain('Flasher', 'Flasher', 'Freeze', 60, 'I am Flash', 70, 'fly')
vill.gen_x()
print(villain.crit(Hero2))
print(vill.gen_x())
