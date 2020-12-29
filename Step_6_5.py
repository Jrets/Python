"""5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних
класса Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом
из классов реализовать переопределение метода draw. Для каждого
из классов методы должен выводить уникальное сообщение. Создать
экземпляры классов и проверить, что выведет описанный метод
для каждого экземпляра."""


class Stationery:
    title = 0
    def draw(self):
        return print(f' запуск отрисовки ')


class Pen(Stationery):

    title = "ручкой"

    def draw(self):
        return print(f' {self.title}')


class Pencil(Stationery):

    title = "карандашом"

    def draw(self):
        return print(f' {self.title}')


class Handle(Stationery):

    title = "маркером"

    def draw(self):
        return print(f' {self.title}')


stationery = Stationery()

pen = Pen()
f'{stationery.draw()} {pen.draw()}'

pencil = Pencil()
f'{stationery.draw()} {pencil.draw()}'

handle = Handle()
f'{stationery.draw()} {handle.draw()}'

