# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = home
        self.food = 0

    def __str__(self):
        return 'Я - {}, сытость {}, радость {}'.format(
            self.name, self.fullness, self.happiness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='cyan')
            self.fullness += 30
            self.house.food -= 30
            self.food += 30
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def pet_the_cat(self):
        cprint('{} гладил кота'.format(self.name), color='yellow')
        self.happiness += 5
        self.fullness -= 10

    def act(self):
        if self.house.dirt >= 90:
            self.happiness -= 10
        if self.fullness < 0:
            cprint('{} умер от голода...'.format(self.name), color='grey')
        elif self.happiness < 10:
            cprint('{} покончил жизнь самоубийством...'.format(self.name), color='grey')
            return


class Husband(Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.earn_money = 0

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        dice = randint(1, 4)
        if self.fullness <= 10:
            super().eat()
        elif self.house.money <= 100:
            self.work()
        elif self.happiness <= 15:
            self.gaming()
        elif dice == 1:
            self.pet_the_cat()
        elif dice == 2:
            self.gaming()
        elif dice == 3:
            self.gaming()
        else:
            self.work()

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='green')
        self.house.money += 150
        self.earn_money += 150
        self.fullness -= 10
        self.happiness -= 10

    def gaming(self):
        cprint('{} расхерачил пидорасов в WOT'.format(self.name), color='red')
        self.happiness += 20
        self.fullness -= 10


class Wife(Man):

    def __init__(self, name):
        super().__init__(name=name)
        self.fur = 0

    def __str__(self):
        return super().__str__()

    def act(self):
        super().act()
        dice = randint(1, 3)
        if self.fullness <= 10:
            super().eat()
        elif self.house.food <= 60:
            self.shopping()
        elif self.house.cat_food <= 10:
            self.shopping()
        elif self.house.dirt >= 100:
            self.clean_house()
        elif self.house.money >= 500:
            self.buy_fur_coat()
        elif self.happiness <= 15:
            self.pet_the_cat()
        elif dice == 1:
            self.pet_the_cat()
        else:
            self.watch_tv()

    def shopping(self):
        if self.house.money >= 60:
            cprint('{} сходила в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 60
            self.house.food += 50
            self.house.cat_food += 10
            self.fullness -= 10
        else:
            cprint('{} деньги кончились'.format(self.name), color='red')

    def buy_fur_coat(self):
        cprint('{} купила шубу'.format(self.name), color='magenta')
        self.house.money -= 350
        self.happiness += 60
        self.fullness -= 10
        self.fur += 1

    def clean_house(self):
        cprint('{} убралась в доме'.format(self.name), color='blue')
        self.house.dirt -= 100
        self.fullness -= 10
        self.happiness -= 20

    def watch_tv(self):
        cprint('{} смотрела TV'.format(self.name), color='green')
        self.fullness -= 10
        self.happiness += 20


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return 'В доме осталось {} еды,{} денег, {} грязи, {} еды кота'.format(
            self.food, self.money, self.dirt, self.cat_food)

    def act(self):
        self.dirt += 5


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = home

    def __str__(self):
        return 'Я - кот {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            cprint('Кот {} поел'.format(self.name), color='cyan')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def vandalism(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint('Кот {} подрал обои.'.format(self.name), color='red')

    def sleep(self):
        self.fullness -= 10
        cprint('Кот {} поспал.'.format(self.name), color='blue')

    def act(self):
        if self.fullness <= 0:
            cprint('Кот {} умер...'.format(self.name), color='grey')
            return
        dice = randint(1, 6)
        if self.fullness <= 20:
            self.eat()
        elif dice == 1:
            self.vandalism()
        elif dice == 2:
            self.vandalism()
        else:
            self.sleep()


class Child(Man):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness < 0:
            cprint('{} умер от голода...'.format(self.name), color='grey')
        if self.fullness <= 10:
            super().eat()
        else:
            self.sleep()

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='cyan')
            self.fullness += 30
            self.house.food -= 10
            self.food += 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def sleep(self):
        self.fullness -= 10
        cprint('Ребёнок {} поспал.'.format(self.name), color='blue')


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
bozon = Cat(name='Бозон')
vasya = Child(name='Вася')

for day in range(1, 366):
    cprint('================== День {} =================='.format(day), color='red')
    home.act()
    serge.act()
    masha.act()
    bozon.act()
    vasya.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(bozon, color='cyan')
    cprint(vasya, color='cyan')
    cprint(home, color='cyan')

print('Серёжа за год заработал {} рублей'.format(serge.earn_money))
print('Было съедено {} еды'.format(serge.food))
print('Маша купила {} шуб'.format(masha.fur))
