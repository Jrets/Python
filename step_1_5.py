proceeds = int(input('введите сумму выручки '))
costs = int(input("введите сумму издержек "))
fin_rez = proceeds - costs
if fin_rez < 0:
    print('шеф, все пропало, убыток составил', fin_rez)
else:
    print('прибыль составила ', fin_rez)
    rent = int(float(fin_rez / proceeds) * 100)
    print('рентабельность составила ', rent, '%')
    kol_sotr = int(input('введите количество сотрудников '))
    prib_sotr = fin_rez / kol_sotr
    print('выручка на одного сотрудника составляет ', prib_sotr)
