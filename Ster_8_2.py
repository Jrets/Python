"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
 Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться
 с ошибкой."""

class DivByZero:
    def __init__(self, dividend,divider ):
        self.dividend = dividend
        self.divider = divider

    @staticmethod
    def check_div_null(dividend, divider):
        try:
            return dividend / divider
        except:
            return 'делить на ноль нельзя'


num = DivByZero(10, 100)
print(num.check_div_null(100, 4))
print(num.check_div_null(10, 0))
print(DivByZero.check_div_null(10, 0))
print(DivByZero.check_div_null(20, 0.4))


