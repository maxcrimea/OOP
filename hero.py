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


Hero = SuperHero('Flasher', 'Flasher', 'Freeze', 100, 'I am Flash') # передал значения в объект класса для проверки работы кода

Hero.show_name()
print(Hero.mul())
print(Hero)
print(len(Hero))
