r_list = [7, 5, 3, 3, 2]
r_bal = int(input("введите рейтинговый бал "))
#   вариант №1
#   r_list.append(r_bal)
print('список до изменения ', r_list)
#   r_list.sort(reverse=True)
#   print(r_list)

for el in range(len(r_list)):
    if r_list[0] < r_bal:   # чтобы не обрабатывать весь массив, если значение
        r_list.insert(0, r_bal)     # превышает максимальное значение списка
        break
    elif r_list[-1] > r_bal:    # чтобы не обрабатывать весь массив, если значение
        r_list.append(r_bal)    # меньше минимального значения списка
        break
    elif r_list[el] == r_bal:   # если значение совпадает с уже имеющимся в списке
        r_list.insert(el+1, r_bal)
        break
    #   elif r_bal in r_list:
    #    r_list.insert(-r_list[::-1].index(r_bal), r_bal) #не смог понять смысл, но понравилось, прокомментируете?
    elif r_list[el] > r_bal and r_list[el+1] < r_bal:   # поиск места вставки
        r_list.insert(el+1, r_bal)  # вставляем элемент
        break
print('список после изменения ', r_list)
