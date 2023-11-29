class Person:
    def __init__(self, name: str, health: int, magic: int):
        self.name = name
        self.health = health
        self.magic = magic

    def get_health(self, inc_health):
        self.health += inc_health
        print(f'Ваше здоровье пополнено на {inc_health} и равно {self.health}')

    def health_reduction(self, red_health):
        self.health -= red_health
        print(f'Ваше здоровье уменьшено на {red_health} и равно {self.health}')

    def magic_show(self):
        print(f'Текущий запас для использования магии составляет {self.magic}')


class Wizard(Person):
    def use_magic(self, cost):
        self.magic += cost
        print(f'Использовано {cost} очков магии и текущий запас составляет {self.magic}')


class Enemy(Person):
    def damage_count(self, damage):
        self.health -= damage
        print(f'Нанесено {damage} очков урона и текущий запас здоровья составляет {self.health}')


person_game = Person(name='Alice', health=100, magic=777)
person_game.get_health(inc_health=50)
person_game.health_reduction(red_health=25)
person_game.magic_show()
wizard_game = Wizard(name='Arthas', health=200, magic=666)
wizard_game.use_magic(cost=100)
enemy_game = Enemy(name='Volondemort', health=600, magic=666)
enemy_game.damage_count(damage=500)
