"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие
атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда). Опишите несколько
дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте
в базовый класс метод show_speed, который должен показывать текущую скорость
автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости."""


class Car:

    def __init__(self, speed: float, color: str, name: str, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        if direction not in ('налево', 'направо'):
            print(f"'{direction}' неверное указание")
            return

        self.direction = direction

        return f'{self.name}  поворот {direction}'

    def show_speed(self):
        return f' скорость {self.name} составляет {self.speed}'


class TownCar(Car):

    def show_speed(self):
        max_speed_allowed = 40
        if self.speed > max_speed_allowed:
            return print("превышение скорости")


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        max_speed_allowed = 60
        if self.speed > max_speed_allowed:
            prev = float(self.speed) - float(max_speed_allowed)
            return f' у {self.name} превышение скорости на ({prev} км/ч)'



class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейский автомобиль'
        else:
            return f'{self.name} не полицейский автомобиль'


austin = TownCar(40, 'Черный', 'Austin_FX4', False)
bentley = WorkCar(70, 'Белый', 'Bentley', True)
bmw = SportCar(120, 'Синий', 'BMW', False)
dodge = PoliceCar(140, ':Желтый', 'Dodge', True)


print(f' {bentley.go()}, {bentley.turn("направо")}')
print(f'{austin.turn("налево")}, {bmw.stop()}')
print(f'{bentley.go()} со скоростью {bentley.speed}, {bentley.show_speed()}')
print(f'{dodge.name} {dodge.color}, {bentley.name} {bentley.color} ')
print(f'{bmw.name} полицейская машина? {bmw.is_police}')
print(f'{bentley.name}  полицейская машина? {bentley.is_police}')
print(dodge.show_speed())
print(bmw.show_speed())
print(f'{dodge.name} полицейская машина? {dodge.is_police}')

