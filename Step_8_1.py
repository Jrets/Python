"""1. Реализовать класс «Дата», функция-конструктор которого должна принимать
 дату в виде строки формата «день-месяц-год». В рамках класса реализовать два
метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год
и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа,
месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных."""

class DateInput:
    def __init__(self, dd_mm_yy):
        self.dd_mm_yy = str(dd_mm_yy)

    @classmethod
    def transform(cls, dd_mm_yy):
        date_number = dd_mm_yy.split('-')
        return int(date_number[0]), int(date_number[1]), int(date_number[2])

    @staticmethod
    def validation(dd_mm_yy):
        date_number = dd_mm_yy.split('-')
        if int(date_number[0]) <=0 or int(date_number[0]) > 31:
            return f' день даты введен некорректно'
        elif int(date_number[1]) <= 0 or int(date_number[1]) > 12:
            return f' номер месяца введен некорректно'
        elif int(date_number[2]) > 2021:
            return f' год введен некорректно'
        else: return f'дата введена корректно'


Date_sourse = DateInput(20-11-20)
print(Date_sourse.transform('20-11-21'))
print('проверка на число: ', sum(Date_sourse.transform('20-11-21')))
print(DateInput.transform('11-11-2011'))
print('проверка на число: ', sum(DateInput.transform('11-11-2011')))
print('проверка на корректность ввода: ', Date_sourse.validation('10-12-20'))
