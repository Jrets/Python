n_month = int(input('Введите номер месяца '))
#   простое решение только через dict
#   my_dict = {1:"зима", 2:"зима", 3:"весна", 4:"весна", 5:"весна", 6:"лето", 7:"лето",\
#   8:"лето", 9:"осень", 10:"осень", 11:"осень", 12:"зима", }
#   print(my_dict.get(n_month))
season_dict = {"зима":  [1, 2, 12], "весна":    [3, 4, 5], "лето":  [6, 7, 8], "осень": [9, 10, 11]}
season_list = [["зима",  [1, 2, 12]], ["весна",    [3, 4, 5]], ["лето",  [6, 7, 8]], ["осень", [9, 10, 11]]]
for season, months in season_list:
    if n_month in months:
        print(f'Шаман предсказал, что это, {season}')
for season, months in season_dict.items():
    if n_month in months:
        print(f'В отрывном календаре, написано, что это {season}')





