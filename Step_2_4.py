w_str = input('введите через пробел самые длинные слова, которые знаете ')
w_list = list(w_str.split())    # преобразуем строку в список по разделителю-пробелу
#   print(type(w_list)) # проверка на тип
for num, elem in enumerate(w_list, 1):  # вывод нумерованого списка, нумерация с 1
    print(num, elem[0:10])  # элемент обрезать до 10 символов
