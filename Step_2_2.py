Name1 = input("Введите Имя ")
Name2 = input("Введите фамилию ")
Bd_Year = int(input("Введите год рождения "))
Sex = input("Введите пол м / ж ")
Rost = float(input("Введите рост "))
Ves = float(input("Введите вес "))
vegan = input("вы веган? да/нет ")
data_user = [Name1.title(), Name2.title(), Bd_Year, Sex, Rost, Ves, vegan]   # составил список
print(data_user)    # вывод списка до изменения
n_el = 0 # номер начального элемента для замен
for index in range(int(len(data_user)/2)):  # определяем количество замен. Последний нечетный элемент избегает замены
    data_user[n_el], data_user[n_el+1] = data_user[n_el+1], data_user[n_el]    # меняем четные на нечетные
    n_el += 2   # переходим к следующему элементу.
print(data_user)    # вывод списка после изменения
