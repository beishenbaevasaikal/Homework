class SuperHero:
    people='people'

    def __init__(self, name, nickname, superpower, health_point, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_point = health_point
        self.catchphrase = catchphrase
    def get_name(self):
        return self.name

    def double_health(self):
        return (self.health_point * 2)

    def __str__(self):
        return (f' Nickname: {self}, Superpower: {self.superpower}, Health_point: {self.health_point}')

    def __len__(self):
        return len(self.catchphrase)

hero = SuperHero("Сайтама", 'Ванпанчмен', 'Невероятная сила', '100', 'Комары...Бесят!')
print('Имя героя - ', hero.get_name())
print('2х здоровья - ', hero.double_health())
print(f'Прозвище героя - {hero.nickname}, суперсила - {hero.superpower}, здоровье героя - {hero.health_point}')
print(f'Коронная фраза - {hero.catchphrase}\n'
      f'длина коронной фразы - ', len(hero.catchphrase))