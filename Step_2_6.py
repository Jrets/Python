prod_list = []
num = 1
while True:
    наименование = input('Введите название: ')
    цена = input('Введите цену: ')
    количество = input('Введите количество: ')
    ед = input('Введите единицу измерения: ')
    тег = input('Введите тег: ')
    prod_list.append((
        num, {
            'наименование': наименование,
            'цена': цена,
            'количество': количество,
            'ед': ед,
            'тег': тег
            }
    ))

    наименование, цена, количество, ед, тег = None, None, None, None, None
    num += 1
    print(prod_list)

    q = input('Продолжить формирование списка? (да/нет)) ')
    if q.lower() == 'нет':
        break

analis = {
    'наименование': [],
    'цена': [],
    'количество': [],
    'ед': set(),
    'тег': set()
}

for el, item in prod_list:
    analis['наименование'].append(item['наименование'])
    analis['цена'].append(item['цена'])
    analis['количество'].append(item['количество'])
    analis['ед'].add(item['ед'])
    analis['тег'].add(item['тег'])
print(analis)
