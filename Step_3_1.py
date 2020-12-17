def rez(var1=0, var2=0):
    var1 = input("Введите делимое ")
    if not var1.isdigit():
        return 'введенные данные не являются числом'
    else:
        var1 = float(var1)
    var2 = input("Введите делитель ")
    if not var2.isdigit():
        return 'введенные данные не являются числом'
    else:
        var2 = float(var2)
    if var2 == 0:
        return 'делить на 0 нельзя'
    return var1 / var2


print(rez())
