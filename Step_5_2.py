"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке."""

sourse_list = ['Иванов Иван Иванович\n', 'Простой\n']
with open("step_5_2.txt", 'w+') as file_obj:
    file_obj.writelines(sourse_list)
with open("step_5_2.txt") as file_obj:
    lines = 0
    letters = 0
    for line in file_obj:
        lines += line.count("\n")
        letters = line.count(" ")+1
        print(f"В строке содержится {letters} слов(а)")
    print(f"В файле содержится {lines} строк(и)")