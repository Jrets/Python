def my_func1(x, y):
    return 1 / x ** abs(y)


print('вариант 1', my_func1(9, -2))


def my_func2(x, y):
    num = 1
    znamenatel = 1
    while num <= abs(y):
        znamenatel = znamenatel * x
        num = num + 1
    return 1/znamenatel


print('вариант 2', my_func2(9, -2))

print('для сверки', pow(9, -2))
