# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC): # одежда
    name: str

    def __init__(self, name: str):
        self.name = name

    @property
    @abstractmethod
    def calculate(self):
        pass


class Coat(Clothes): # пальто
    _size: float

    def __init__(self, name: str, size: float):
        super().__init__(name)
        self._size = size

    @property
    def calculate(self):
        return round((self._size / 6.5 + 0.5), 2)


class Suit(Clothes): # костюм
    _height: float

    def __init__(self, name: str, height: float):
        super().__init__(name)
        self._height = height

    @property
    def calculate(self):
        return round((2 * self._height + 0.3), 2)


coat = Coat('Пальто', 6.2)
print(f"На пошив {coat.name} потребуется {coat.calculate} метров ткани.")

suit = Suit('Костюм', 0.51)
print(f"На пошив {suit.name}а потребуется {suit.calculate} метров ткани.")