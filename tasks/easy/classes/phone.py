"""
Создать класс Phone, у которого будут следующие атрибуты:

Определить атрибуты:

- brand - бренд
- model - модель
- issue_year - год выпуска

Определить методы:

- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""


class Phone:
    brand = 'бренд'
    model = 'модель'
    issue_year = 'год выпуска'


def __init__(self, brand, model, issue_year):
    self.brand = brand
    self.model = model
    self.issue_year = issue_year


def __receive_call__(self, name):
    return f"звонит {name}"


def __get_info__(self, brand, model, issue_year):
    return brand, model, issue_year


def __str__(self, brand, model, issue_year):
    print(f'"Бренд": {brand}, "Модель": {model}, "Год выпуска": {issue_year}'.format(self.brand, self.model, self.issue_year))
