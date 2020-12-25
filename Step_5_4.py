"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую
 построчно данные. При этом английские числительные должны заменяться
  на русские. Новый блок строк должен записываться в новый текстовый файл."""

sourse_num = ['One — 1\n', 'Two — 2\n', 'Three — 3\n', 'Four — 4\n']
with open("step_5_4.txt", 'w+') as num_obj:
    num_obj.writelines(sourse_num)

new_num = []    # новый список
dict_num = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open("step_5_4.txt", "r") as num_obj:     # чтение файла
    num_list = num_obj.readlines()  # чтение файла построчно
    for el in num_list:
        el = el.split(" ", 1)   # разбиваем по пробелу, выбираем по индексу
        #   print(el)
        new_num.append(dict_num[el[0]] + " " + el[1])    # формирование нового списка из двух
        #   print(new_num)

with open("step_5_4_new.txt", 'w+') as num_new_obj:     # запись в файл
    num_new_obj.writelines(new_num)  # построчно
    print(new_num)


