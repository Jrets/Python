"""2. Реализовать проект расчета суммарного расхода ткани на производство
одежды. Основная сущность (класс) этого проекта — одежда, которая может
иметь определенное название. К типам одежды в этом проекте относятся
пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих
методов на реальных данных. Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике
работу декоратора @property."""


class Сlothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h

    def cons_coat(self):
        return self.v / 6.5 + 0.5

    def cons_suit(self):
        return self.h * 2 + 0.3

    @property
    def cons_full(self):
        return str(f'Общая площадь ткани \n'
                   f' {round((self.v / 6.5 + 0.5) + (self.h * 2 + 0.3),2)}')


class Coat(Сlothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.cons_coat = round(self.v / 6.5 + 0.5, 2)

    def __str__(self):
        return f'Площадь ткани для пальто {self.cons_coat}'


class Suit(Сlothes):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.cons_suit = round(self.h * 2 + 0.3, 2)

    def __str__(self):
        return f'Площадь ткани для костюма {self.cons_suit}'


coat = Coat(2, 4)
suit = Suit(2, 4)
print(coat)
print(suit)
print(coat.cons_full)
print(suit.cons_full)
