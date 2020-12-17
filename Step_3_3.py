def my_func(var1, var2, var3):
    spisok = [var1, var2, var3]
    vyborka = []
    max_1 = max(spisok)
    vyborka.append(max_1)
    spisok.remove(max_1)
    max_2 = max(spisok)
    vyborka.append(max_2)
    print(sum(vyborka))


my_func(-1, 4, 0)
