"""1. Создать программно файл в текстовом формате, записать в него
 построчно данные, вводимые пользователем. Об окончании ввода данных
 свидетельствует пустая строка."""

source_list = []
while True:
    str_vvod = input("Введите данные построчно. Для окончания введите пустую строку ")
    if str_vvod == "":
        exit()
    else:
        str_line = str_vvod + '\n'
        source_list.append(str_line)

    with open("step_5_1.txt", "w") as file_obj:
       file_obj.writelines(source_list)
