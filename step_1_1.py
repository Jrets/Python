#1.1
integer = 5
print("Целое число: ", integer)
floating_point_number = 4.8
print("Число с плавающей запятой:", floating_point_number)
stroka = "Сумма двух чисел"
sum_two_numbers = integer + floating_point_number
print(stroka, sum_two_numbers)
print("Для регистрации укажите информацию: ")
name1 = input("Имя ")
print(name1)
name2 = input("Фамилия ")
print(name2)
print("Укажите дату рождения")
bday_day = input("День ")
bday_month = input("Месяц ")
bday_year = input("Год ")
bday_data = bday_day+"."+bday_month+"."+bday_year
user_data = "Проверьте введенные данные " + name1 +" " + name2 +" Дата рождения " +bday_data +"г."
print(f"{user_data}")








