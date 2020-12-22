def zp(work_time=0, rate_hour=0, bonus =0):
    work_time = input("Введите отработанное время ")
    if not work_time.isdigit():
        return 'введенные данные не являются числом'
    else:
        work_time = float(work_time)
    rate_hour = input("Укажите почасовую ставку ")
    if not rate_hour.isdigit():
        return 'введенные данные не являются числом'
    else:
        rate_hour = float(rate_hour)
    bonus = input("Введите размер премии ")
    if not bonus.isdigit():
        return 'введенные данные не являются числом'
    else:
        bonus = float(bonus)

    return work_time * rate_hour + bonus


def gen_int(start_num, stop_num):
    from itertools import count
    for el in count(start_num):
        if el > stop_num:
            break
        else:
            print(el)


def repeat_list(sourse_list, iteration):
    from itertools import cycle
    i = 0
    iter = cycle(sourse_list)
    while i < iteration:
        print(next(iter))
        i += 1


