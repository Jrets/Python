"""6. Реализовать функцию int_func(), принимающую слово из маленьких
 латинских букв и возвращающую его же, но с прописной первой буквой.
  Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из
 слов, разделенных пробелом. Каждое слово состоит из латинских букв в
 нижнем регистре. Сделать вывод исходной строки, но каждое слово должно
  начинаться с заглавной буквы. Необходимо использовать написанную ранее
   функцию int_func()."""

def int_func(*words):
    stroka = input("Введите слова из строчных латинских букв: ")
    if not stroka.islower():
        return print("введенная последовательность состоит не только строчных из букв ")
    return print(stroka.title())


print(int_func())
