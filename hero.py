class SuperHero:
    people = 'people'
    """Родительский класс супергероев"""

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def show_name(self):
        print(f'Name: {self.name}')

    def mul(self):
        self.health_points = self.health_points * 2
        """Умножает хп героя на 2"""

    def __str__(self):
        return f'{self.nickname} {self.superpower} {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero('Flasher', 'Flash', 'Freeze', 100, 'I am Flash')

hero.show_name()
hero.mul()
print(hero)
print(len(hero))


class Hero2(SuperHero):
    costume = True
    """Класс супергероя 2 (носит костюм)"""

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def mul(self):
        self.fly = True
        self.health_points = pow(self.health_points, 2)
        """Возводит хп героя в квадрат"""

    def view_fly(self):
        print('fly in the True_phrase')


ironman = Hero2('Tony Stark', 'Iron Man', 'fly & power', 100, 'I am Iron Man!', 15, 'fly')
ironman.mul()
ironman.view_fly()
print(ironman)


class Hero3(SuperHero):
    cape = True
    """Класс супергероя 3 (есть плащь)"""

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage=False, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def mul(self):
        self.fly = True
        self.health_points = pow(self.health_points, 2)
        """Возводит хп героя в квадрат"""

    def view_fly(self):
        print('fly in the True_phrase')


superman = Hero3('Kal-El', 'Superman', 'very strong', 100, 'a job for Superman', 18, 'fly')
superman.mul()
superman.view_fly()
print(superman)


class Villain(Hero3):
    people = 'monster'
    """Класс супергероя монстра"""

    def gen_x(self):
        return None

    def crit(self, damage_crit):
        damage_crit.health_points = damage_crit.health_points - pow(self.damage, 3)
        return f'теперь хп у {damage_crit.nickname} = {damage_crit.health_points}'
    """Возводит в степень урон"""


beast = Villain('Hank', 'Beast', 'Superhuman strength', 100, 'I am The Beast', 13, 'fly')
print(beast)
print(beast.crit(superman))
